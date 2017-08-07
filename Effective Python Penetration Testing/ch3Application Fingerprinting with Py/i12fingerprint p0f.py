from scapy.all import *
from scapy.modules.p0f import *

conf.p0f_base ="/etc/p0f/p0f.fp"
conf.p0fa_base ="/etc/p0f/p0fa.fp"
conf.p0fr_base ="/etc/p0f/p0fr.fp"
conf.p0fo_base ="/etc/p0f/p0fo.fp"
sniff(prn=prnp0f)