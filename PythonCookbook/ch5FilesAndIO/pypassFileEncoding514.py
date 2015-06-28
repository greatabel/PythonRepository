#encoding:utf-8
from colorama import Fore, Back, Style



def main():
    import sys
    print(sys.getfilesystemencoding())

    with open('test.txt','w') as f:
        f.write('Spicy!')

    with open('test.txt') as f:
        print(f.read())




            
if __name__ == '__main__':
    main()
