#encoding:utf-8
#http://stackoverflow.com/questions/11914472/stringio-in-python3
from colorama import Fore, Back, Style
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

def main():
    s = StringIO()
    s.write("test")
    print(" test1",file=s)
    print(s.getvalue())

    s = StringIO("test2 test3")
    print(s.read(4))
    print(s.read())

            
if __name__ == '__main__':
    main()


