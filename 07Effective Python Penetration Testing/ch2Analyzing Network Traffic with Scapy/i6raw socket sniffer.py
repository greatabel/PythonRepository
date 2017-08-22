import socket #Imported sockets module
import struct
import binascii
import sys

try:
   #Create an raw socket
    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                  socket.htons(0x0800))
except socket.error as e:
    print('Error occurred while creating socket. Error code: ' + str(e))
    sys.exit()

while True:
    packet = raw_socket.recvfrom(2048)
    ethernet_header = packet[0][0:14]
    eth_header = struct.unpack("!6s6s2s", ethernet_header)
    print("destination:" + binascii.hexlify(eth_header[0]) + " Source:" +
    binascii.hexlify(eth_header[1]) +  " Type:" +
    binascii.hexlify(eth_header[2]) )
    ip_header = packet[0][14:34]
    ip_hdr = struct.unpack("!12s4s4s", ip_header)
    print("Source IP:" + socket.inet_ntoa(ip_hdr[1]) + " Destination IP:" +
      socket.inet_ntoa(ip_hdr[2]))
