import colorama
from colorama import Fore, Back, Style




def main():
    a = [1,20,300,4000]
    f = open('passwd.txt')
    for line in reversed(list(f)):
        print('reversed=',line,end='')
    print(Fore.GREEN + "more accurate" + Style.RESET_ALL)
    for x in reversed(a):
        print(x)
            
if __name__ == '__main__':
    main()

