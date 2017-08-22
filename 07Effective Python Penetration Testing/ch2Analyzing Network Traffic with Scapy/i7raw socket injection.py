import socket #Imported sockets module
import struct
import sys


try:
 #Create an raw socket
    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW,
      socket.htons(0x0800))
except socket.error as e:
    print('Error occurred while creating socket. Error code: ' + str(e) )
sys.exit()

raw_socket.bind(("wlan0", socket.htons(0x0800)))
packet =  struct.pack("!6s6s2s", '\xb8v?\x8b\xf5\xfe',
'l\x19\x8f\xe1J\x8c', '\x08\x00')
raw_socket.send(packet + "Hello")
