#encoding:utf-8
from colorama import Fore, Back, Style

def avg(first, *rest):
    return (first + sum(rest))/(1 + len(rest))

import html
def recv(maxsize,*,block):
    'recv a message'
    pass

def minum(*values,clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

def main():
    # recv(1024,True)
    recv(1024,block=True)

    print(Fore.BLUE + "other way:" + Style.RESET_ALL)
    minum(1,-2,5,10)
    minum(1,-2,5,10,clip=0)
    


    print(Back.GREEN + 'demo2'+ Back.RESET)






            
if __name__ == '__main__':
    main()
