import dpkt
import sys, datetime, socket, math
from datetime import datetime, timedelta



USAGE = "\npython3 \t aassignment2.py <PCAP FILE> [SRC_IP] [DEST_IP]\n Source and destination IP is optional. \n"

SRC_IP = "130.245.145.12"
DST_IP = "128.208.2.198"


def my_flow(pcap):
    my_dict = {}
    total_flows = 0
    for t, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        if eth.data.p != dpkt.ip.IP_PROTO_TCP:
            continue
        src = socket.inet_ntoa(eth.ip.src)
        dst = socket.inet_ntoa(eth.ip.dst)
        tcp = eth.ip.data
        syn = (tcp.flags & dpkt.tcp.TH_SYN) != 0
        ack = (tcp.flags & dpkt.tcp.TH_ACK) != 0
        fin = (tcp.flags & dpkt.tcp.TH_FIN) != 0
        pkt_dict = {
            "syn": syn,
            "ack": ack,
            "fin": fin,
            "src": socket.inet_ntoa(eth.ip.src),
            "dst": socket.inet_ntoa(eth.ip.dst),
            "tcp": eth.ip.data,
            "timestamp": t,
        }
        if src == SRC_IP and dst == DST_IP:
            if syn:
                total_flows += 1
                syn_dict = {
                    "flow_start": t,
                    "flow": [pkt_dict],
                    "scale": tcp.opts[-1],
                    "iseq": tcp.seq,
                }
                if tcp.sport in my_dict:
                    my_dict[tcp.sport].append(syn_dict)
                else:
                    my_dict[tcp.sport] = [syn_dict]
            else:
                if tcp.sport in my_dict:
                    syn_dict = max(my_dict[tcp.sport], key=lambda x: x["flow_start"])
                    syn_dict["flow"].append(pkt_dict)
        elif src == DST_IP and dst == SRC_IP:
            if tcp.dport in my_dict:
                syn_dict = max(my_dict[tcp.dport], key=lambda x: x["flow_start"])
                if not syn_dict.get("iack", False):
                    syn_dict["iack"] = tcp.seq
                syn_dict["flow"].append(pkt_dict)
    flow_lst = []
    for f in my_dict.values():
        flow_lst.extend(f)
    return sorted(flow_lst, key=lambda f: f["flow_start"]), total_flows


def flow_analyzer(pcap, max_pkt_per_flow=2, max_cwnd_rtt_count=5):
    TCP_FLOWS_T = my_flow(pcap)

    print("TCP Flows: %s\n" % TCP_FLOWS_T[1])
    for flow in TCP_FLOWS_T[0]:
        setup = 0
        src_c = 0
        dst_c = 0
        total_data = 0

        cwnd_i = 0
        cwnd_lst = [0] * max_cwnd_rtt_count
        pkt_buf = []

        ack_dict = {}

        triple_dup_acks = 0
        timeouts = 0
        fast_retransmit = 0

        rtt_prime = 0
        rtt_old = 0
        WEIGHT = 0.125

        time_dict = {}
        time_ack = 0

        start_time = datetime.fromtimestamp(flow["flow_start"])
        sorted_flows = sorted(flow["flow"], key=lambda x: x["timestamp"])
        for ip_i, ip in enumerate(sorted_flows):
            src = ip["src"]
            dst = ip["dst"]
            tcp = ip["tcp"]
            syn = ip["syn"]
            ack = ip["ack"]
            fin = ip["fin"]
            rwnd = tcp.win << flow["scale"]
            if src == SRC_IP and dst == DST_IP:
                total_data += int(len(tcp.data) + (tcp.off * 4))
                if syn:
                    print(
                        "\n--- Start flow %s:%s -> %s:%s ---\n"
                        % (src, tcp.sport, dst, tcp.dport)
                    )
                    time_dict[tcp.seq + 1] = ip["timestamp"]
                    setup += 1
                elif ack and not fin:
                    if setup == 2:
                        setup += 1
                    elif setup == 3:
                        if src_c < max_pkt_per_flow:
                            print(
                                "[%s:%s -> %s:%s]\nSEQ=%s (Relative=%s), ACK=%s (Relative=%s), RWND=%s\n"
                                % (
                                    src,
                                    tcp.sport,
                                    dst,
                                    tcp.dport,
                                    tcp.seq,
                                    tcp.seq - flow["iseq"],
                                    tcp.ack,
                                    tcp.ack - flow["iack"],
                                    rwnd,
                                )
                            )
                            src_c += 1
                        if tcp.seq + len(tcp.data) in time_dict:
                            if fast_retransmit == tcp.seq:
                                triple_dup_acks += 1
                                fast_retransmit = 0
                            elif (
                                ip["timestamp"] - time_dict[tcp.seq + len(tcp.data)]
                            ) > rtt_prime:
                                timeouts += 1
                        else:
                            time_dict[tcp.seq + len(tcp.data)] = ip["timestamp"]
                        if cwnd_i < max_cwnd_rtt_count:
                            pkt_buf.append(tcp.seq)
                    else:
                        print("\n--- End flow (Handshake didn't finish) ---\n")
                        break
                elif fin:
                    print("\nTotal data sent: %s bytes" % total_data)
                    end_time = datetime.fromtimestamp(sorted_flows[-1]["timestamp"])
                    delta = (end_time - start_time) / timedelta(milliseconds=1)
                    print(
                        "Total time between first sent byte and last ack: %.2f ms"
                        % delta
                    )
                    print("Sender throughput: %.2f bytes/ms\n" % (total_data / delta))

                    for i, c in enumerate(cwnd_lst):
                        if c == 0:
                            break
                        change = ""
                        if c == cwnd_lst[0]:
                            change = " (cwnd = icwnd)"
                        elif c > cwnd_lst[i - 1]:
                            change = " (cwnd += %s)" % (c - cwnd_lst[i - 1])
                        elif c < cwnd_lst[i - 1]:
                            change = " (cwnd -= %s)" % (cwnd_lst[i - 1] - c)
                        print(
                            "My guess size of cwnd %s: %s packets%s"
                            % (i + 1, cwnd_lst[i], change)
                        )
                    print(
                        "\nRetransmission due to triple duplicate acks: %s"
                        % (
                            # len(list(filter(lambda x: x >= 3, ack_dict.values())))
                            triple_dup_acks
                        )
                    )
                    print("Retransmission due to timeouts: %s" % timeouts)
                    print(
                        "\n--- End flow %s:%s -> %s:%s ---\n"
                        % (src, tcp.sport, dst, tcp.dport)
                    )
                    break
            elif src == DST_IP and dst == SRC_IP:
                if syn:
                    rtt_old = ip["timestamp"] - time_dict[tcp.ack]
                    rtt_prime = rtt_old
                    setup += 1
                elif ack:
                    if dst_c < max_pkt_per_flow:
                        print(
                            "[%s:%s <- %s:%s]\nSEQ=%s (Relative=%s), ACK=%s (Relative=%s), RWND=%s\n"
                            % (
                                dst,
                                tcp.dport,
                                src,
                                tcp.sport,
                                tcp.seq,
                                tcp.seq - flow["iack"],
                                tcp.ack,
                                tcp.ack - flow["iseq"],
                                rwnd,
                            )
                        )
                    if tcp.ack in time_dict:
                        rtt_old = rtt_prime
                        rtt_prime = ((1 - WEIGHT) * rtt_old) + (
                            WEIGHT * (ip["timestamp"] - time_dict[tcp.ack])
                        )

                    if (
                        math.isclose(
                            (cwnd_i + 2) * rtt_prime,
                            ip["timestamp"] - flow["flow_start"],
                            rel_tol=1e-2,
                        )
                        and cwnd_i < max_cwnd_rtt_count
                        and sorted_flows[ip_i + 1]["src"] == SRC_IP
                    ):
                        pkt_buf = list(filter(lambda x: x >= tcp.ack, pkt_buf))
                        buf_size = len(pkt_buf) + 1
                        cwnd_lst[cwnd_i] = (
                            (
                                buf_size
                                if ((cwnd_i == 0) or (buf_size > cwnd_lst[cwnd_i - 1]))
                                else cwnd_lst[cwnd_i - 1]
                            )
                            if (cwnd_lst[cwnd_i] == 0)
                            else cwnd_lst[cwnd_i]
                        )
                        cwnd_i += 1

                    if tcp.ack in ack_dict:
                        ack_dict[tcp.ack] += 1
                        if ack_dict[tcp.ack] == 3:
                            fast_retransmit = tcp.ack
                    else:
                        ack_dict[tcp.ack] = 0
                    dst_c += 1
        else:
            continue


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print(USAGE)
        exit(0)
    if len(sys.argv) == 3:
        SRC_IP = sys.argv[2]
    if len(sys.argv) == 4:
        DST_IP = sys.argv[3]
    f = open(sys.argv[1], "rb")
    pcap = None
    try:
        pcap = dpkt.pcap.Reader(f)
    except:
        print("ERROR: Invalid pcap file (%s)" % sys.argv[1])
        exit(0)
    flow_analyzer(pcap)


if __name__ == "__main__":
    main()
