import socket #Imported sockets module
import sys
TCP_IP = '127.0.0.1'
TCP_PORT = 8090 #Reserve a port
BUFFER_SIZE = 1024
MESSAGE_TO_SERVER = b"Hello, World!"

try:
   #Create an AF_INET (IPv4), STREAM socket (TCP)
   tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
   print('Error occurred while creating socket. Error code: ' + str(e[0])
        + ' , Error message : ' + e[1] )
   sys.exit()

tcp_socket.connect((TCP_IP, TCP_PORT))
try :
   #Sending message
   tcp_socket.send(MESSAGE_TO_SERVER)
except socket.error as e:
   print('Error occurred while sending data to server. Error code: ' +
  str(e[0]) + ' , Error message : ' + e[1])
   sys.exit()

print('Message to the server send successfully')
data = tcp_socket.recv(BUFFER_SIZE)
tcp_socket.close()
print("Response from server:", data)