from scapy.all import * #Import Scapy

# sudo python3 i8dns_scrapy.py 


# Create a DNS request Packet to 8.8.8.8
dns_packet = IP(dst="115.182.201.8")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="douban.com"))
# Send packet and get the response
dns_request = sr1(dns_packet,verbose=1)
# Print the response
print('#'*10, dns_request[DNS].summary() )