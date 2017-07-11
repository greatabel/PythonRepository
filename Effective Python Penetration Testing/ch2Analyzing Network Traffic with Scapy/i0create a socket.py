import socket 
import sys

try:
    # create an AF_INET (IPv4), Stream socket (TCP)
    tcp_socke = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print('Error occured while creating socket. Error code: ' + str(e[0]) +
            ' , Error message: ' + e[1])
    sys.exit()

print("Success!")