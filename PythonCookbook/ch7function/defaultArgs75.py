#encoding:utf-8
from colorama import Fore, Back, Style

def spam(a,b=42):
    print(a,'b=',b)


def main():
    spam(1)
    spam(1,2)

    print(Fore.BLUE + "other way:" + Style.RESET_ALL)
   
    


    print(Back.GREEN + 'demo2'+ Back.RESET)






            
if __name__ == '__main__':
    main()
