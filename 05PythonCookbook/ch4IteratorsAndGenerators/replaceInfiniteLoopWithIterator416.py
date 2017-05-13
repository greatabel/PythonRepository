#https://pypi.python.org/pypi/colorama
# 如果发现占用 ps aux | grep <string>
from colorama import Fore, Back, Style

CHUNKSIZE = 8192

def oldReader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        print(data)

def newReader(s):
    for chunk in iter(lambda:s.recv(CHUNKSIZE),b''):
        print('data:',chunk)

def main():
    print(Back.GREEN + 'my way'+Back.RESET )
    
    import socket

    HOST = '127.0.01'    # The remote host
    PORT = 50007              # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    # data = s.recv(1024)
    # data = oldReader(s)
    data = newReader(s)
    s.close()
    print('Received', repr(data))


    
    
    

            
if __name__ == '__main__':
    main()

