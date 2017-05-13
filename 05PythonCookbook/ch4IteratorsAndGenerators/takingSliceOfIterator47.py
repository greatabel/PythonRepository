#https://pypi.python.org/pypi/colorama

from colorama import Fore, Back, Style

def count(n):
    while True:
        yield n
        n += 1




def main():
    print(Back.GREEN + 'and with a green background'+Back.RESET )
    c = count(0)
    # print(c[10:20])
    import itertools
    for x in itertools.islice(c,10,20):
        print(x)
    
    
    

            
if __name__ == '__main__':
    main()

