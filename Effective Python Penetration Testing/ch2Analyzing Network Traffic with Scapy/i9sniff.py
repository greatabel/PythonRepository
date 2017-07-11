from scapy.all import * #Import Scapy
from datetime import datetime


interface = 'en0' #Interface to sniff
filter_bpf = 'udp and port 53' #BPF filter to filter udp packets in port 53


#Runs this for each packet
def select_DNS(packet):
   packet_time = packet.sprintf('%sent.time%')
   try:
       if DNSQR in packet and packet.dport == 53:
       #Print queries
          print('DNS queries Message from '+ packet[IP].src + '\
          to ' + packet[IP].dst +' at ' + packet_time)
       elif DNSRR in packet and packet.sport == 53:
       #Print responses
          print( 'DNS responses Message from '+ packet[IP].src + '\
          to ' + packet[IP].dst +' at ' + packet_time)
   except:
       pass
#Sniff the packets
sniff(iface=interface, filter=filter_bpf, store=0, prn=select_DNS)
