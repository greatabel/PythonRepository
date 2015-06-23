import colorama
from colorama import Fore, Back, Style

def countdown(n):

    print("Starting to count from",n)
    while n>0:
        yield n
        n -= 1
    print("Done!")


def main():
    try:
        c = countdown(3)
        print(next(c))
        print(next(c))
        print(next(c))
        print(next(c))
    except StopIteration:
        print("Error in StopIteration")
    pass
    # print(Fore.BLUE + "demo2:" + Style.RESET_ALL)
    
    

            
if __name__ == '__main__':
    main()

