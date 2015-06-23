import colorama
from colorama import Fore, Back, Style

def frange(start,stop,increment):
    x = start
    while x <= stop:
        yield x
        x += increment


def main():
    for n in frange(0,5,0.5):
        print(n)
    print(Fore.BLUE + "demo2:" + Style.RESET_ALL)
    items = list(frange(0,200,25))
    print(items)
    it = iter(frange(0,100,10))
    print(next(it))
    print(next(it))
    print(next(it))
    

            
if __name__ == '__main__':
    main()

