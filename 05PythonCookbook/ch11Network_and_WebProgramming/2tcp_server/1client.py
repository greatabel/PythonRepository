from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 20000))

s.send(b'Hello\nOne\nTwo')

print('-'*10)

resp = s.recv(8192)
print('Response:', resp)
s.close()

