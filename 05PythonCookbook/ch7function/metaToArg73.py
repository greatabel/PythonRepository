#encoding:utf-8
from colorama import Fore, Back, Style

def add(x:int, y:int) -> int:
    return x + y


def main():
    # recv(1024,True)
    print(add(10,90))
    # print(help(add))
    print(add.__annotations__)

    print(Fore.BLUE + "other way:" + Style.RESET_ALL)
   
    


    print(Back.GREEN + 'demo2'+ Back.RESET)






            
if __name__ == '__main__':
    main()
