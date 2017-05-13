
#encoding:utf-8
#http://stackoverflow.com/questions/11914472/stringio-in-python3
from colorama import Fore, Back, Style
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

def main():
    filepath='58test.txt'
    with open(filepath,"wt") as f:
        f.write('test    0000')
        f.write('test1111')
        f.write('test2222')

    from functools import partial
    RECORD_SIZE = 4
    with open('58test.txt', 'rb') as f:
        records = iter(partial(f.read, RECORD_SIZE), b'') 
        for r in records:
            print(r)
            
if __name__ == '__main__':
    main()


