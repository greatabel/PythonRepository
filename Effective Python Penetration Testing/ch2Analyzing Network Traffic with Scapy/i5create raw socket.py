import socket
import sys


try:
    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, 
                    socket.IPPROTO_RAW)
except socket.error as e:
    print('Error occurred while sending data to server. Error code: ' +
            str(e))
    sys.exit()
