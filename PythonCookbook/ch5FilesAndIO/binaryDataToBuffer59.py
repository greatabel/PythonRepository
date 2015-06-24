#encoding:utf-8
import os.path
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename)) 
    with open(filename, 'rb') as f:
        f.readinto(buf) 
    return buf

def main():
    buf = read_into_buffer('58test.txt')
    print(buf)
    buf[0:5]=b'test1'
    print(buf)


            
if __name__ == '__main__':
    main()
