import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *
# To sniff scapy requires to run as sudo.
# sudo python3 i10OS\ fingerprinting.py 



ans,unans=srloop(IP(dst="192.168.0.1")/TCP(dport=80,flags="S"))
temp = 0
for s,r in ans:
    temp = r[TCP].seq - temp
    print( str(r[TCP].seq) + "\t+" + str(temp) )



