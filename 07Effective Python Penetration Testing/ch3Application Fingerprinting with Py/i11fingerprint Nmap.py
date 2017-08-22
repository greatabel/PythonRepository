from scapy.all import Ether, IP, TCP
from scapy.modules.nmap import *


conf.nmap_base ="/usr/share/nmap/nmap-os-db"
nmap_fp("192.168.0.1")