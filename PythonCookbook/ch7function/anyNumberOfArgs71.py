#encoding:utf-8
from colorama import Fore, Back, Style

def avg(first, *rest):
    return (first + sum(rest))/(1 + len(rest))

def main():
    print(avg(1,2))
    print(avg(1,2,3))

    print(Fore.BLUE + "and content:" + Style.RESET_ALL)

    print(Back.GREEN + 'demo2'+ Back.RESET)




            
if __name__ == '__main__':
    main()
