import socket   #socket模块


HOST='10.0.0.245'
PORT=50007
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #定义socket类型，网络通信，TCP


class NetworkError(Exception):
    pass

class HostnameError(Exception):
    pass

class TimeoutError(Exception):
    pass

class ProtocolError(Exception):
    pass

if __name__ == "__main__":
    try:
        msg = s.recv(1)
    except TimeoutError as e:
        print('1', e)
    except ProtocolError as e:
        print('2', e)
    except Exception as e:
        print('3', e)

