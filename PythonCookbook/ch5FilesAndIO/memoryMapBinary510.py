#encoding:utf-8
import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE): 
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

def main():
    size = 1000
    with open('data', 'wb') as f:
        f.seek(size-1)
        f.write(b'\x00')

    m = memory_map('data')
    print(len(m))
    m[0:11]=b'hello world'
    m.close()

    print('change!')
    with open('data', 'rb') as f:
        print(f.read(100))



            
if __name__ == '__main__':
    main()
