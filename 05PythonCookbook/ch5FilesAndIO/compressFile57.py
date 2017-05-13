#encoding:utf-8
#http://stackoverflow.com/questions/11914472/stringio-in-python3
from colorama import Fore, Back, Style
import gzip
import bz2
def createzip():

    content = b"Lots of content here 1"
    with gzip.open('file.txt.gz', 'wb') as f:
        f.write(content)

def createbz():
    with bz2.open('somefile.bz2', 'wt') as f:
        text = 'test it bz'
        f.write(text)

def main():
    createzip()
    with gzip.open('file.txt.gz','rt') as f:
        text = f.read()
        print('text=',text)
    createbz()
    with bz2.open('somefile.bz2','rt') as f:
        text = f.read()
        print('text=',text)


            
if __name__ == '__main__':
    main()


