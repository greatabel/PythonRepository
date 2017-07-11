import socket #Imported sockets module
import sys
from _thread import *

TCP_IP = '127.0.0.1'
TCP_PORT = 8090 # Reserve a port
try:
   #create an AF_INET (IPv4), STREAM socket (TCP)
   tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
   print('Error occured while creating socket. Error code: ' + str(e[0]) +
         ' , Error message : ' + e[1])
   sys.exit()

#Bind socket to host and port
tcp_socket.bind((TCP_IP, TCP_PORT))
tcp_socket.listen(10)
print('Listening..')

#Function for handling connections. Used to create threads
def ClientConnectionHandler(connection):
   BUFFER_SIZE = 1024
   #Sending message to client
   connection.send(b'Welcome to the server')
   #infinite loop to keep the thread alive.
   while True:
       #Receiving data from client
       data = connection.recv(BUFFER_SIZE)
       reply = b'Data received:' + data
       if not data:
           break
       connection.sendall(reply)
   #Exiting loop
   connection.close()

#keep server alive always (infinite loop)
while True:
   connection, address = tcp_socket.accept()
   print('Client connected:', address)
   start_new_thread(ClientConnectionHandler ,(connection,))

tcp_socket.close()
