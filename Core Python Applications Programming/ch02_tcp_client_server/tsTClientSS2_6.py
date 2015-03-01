from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
 tcpClientSock= socket(AF_INET,SOCK_STREAM)
 tcpClientSock.connect(ADDR)
 data=raw_input('> ')
 if not data:
  break;
 tcpClientSock.send(data+'\n')
 data =tcpClientSock.recv(BUFSIZ)
 if not data:
   break
 print data
 tcpClientSock.close()
