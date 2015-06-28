#encoding:utf-8
from colorama import Fore, Back, Style




def main():
    x = 10
    a = lambda y: x + y
    print(a(10))
    x = 20
    print(a(10))
    x = 30
    print(a(10))
    print(Fore.RED + "other way:" + Style.RESET_ALL)
    
    x = 10
    b = lambda y, x=x : x + y
    
    print(b(10))
    x = 20
    print(b(10))
    x = 30
    print(b(10))

    print(Back.GREEN + 'demo2'+ Back.RESET)

    funcs = [lambda x: x+n for n in range(5)]
    for f in funcs:
        print(f(0))

    funcs=[lambda x,n=n: x+n for n in range(5)]
    for f in funcs:
        print(f(0))
    
   
    









            
if __name__ == '__main__':
    main()
