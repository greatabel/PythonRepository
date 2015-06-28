#encoding:utf-8
from colorama import Fore, Back, Style

def myfun():
    return 1,2,3


def main():
    # recv(1024,True)
    a,b,c = myfun()
    print(a,b,c)
    x = myfun()
    print(x)

    print(Fore.BLUE + "other way:" + Style.RESET_ALL)
   
    


    print(Back.GREEN + 'demo2'+ Back.RESET)






            
if __name__ == '__main__':
    main()
