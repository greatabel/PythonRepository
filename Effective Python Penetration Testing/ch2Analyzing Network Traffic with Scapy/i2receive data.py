import socket #Imported sockets module
TCP_IP = '127.0.0.1'
TCP_PORT = 8090
BUFFER_SIZE = 1024 

#Normally use 1024, to get fast response from the server
# use small size

try:
      #Create an AF_INET (IPv4), STREAM socket (TCP)
      tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
  print('Error occurred while creating socket. Error code: ' + str(e[0]) +
        ' , Error message : ' + e[1])
  sys.exit()

tcp_socket.bind((TCP_IP, TCP_PORT))
# Listen for incoming connections  (max queued connections: 2)
tcp_socket.listen(2)
print('Listening..')
#Waits for incoming connection (blocking call)
connection, address = tcp_socket.accept()
print('Connected with:', address)