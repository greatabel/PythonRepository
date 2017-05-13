#encoding:utf-8
#https://pypi.python.org/pypi/colorama
# 如果发现占用 ps aux | grep <string>
from colorama import Fore, Back, Style


def main():
    filepath = 'sample2.txt'
    with open(filepath,'wt') as f:
        print("hello world!", file=f)
        print("hello world 2!", file=f)
    
    

            
if __name__ == '__main__':
    main()


