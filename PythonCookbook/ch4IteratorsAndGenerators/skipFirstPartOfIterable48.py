#https://pypi.python.org/pypi/colorama

from colorama import Fore, Back, Style


def testA():
    items = ['a','b','c','d',1,2,3,4,5]
    from itertools import islice
    for x in islice(items,2,None):
        print(x)



def main():
    print(Back.GREEN + 'and with a green background'+Back.RESET )
    
    from itertools import dropwhile
    with open('passwd.txt') as f:
        for line in dropwhile(lambda line : line.startswith('#'),f):
            print(line,end='')
    print(Back.RED + 'and with a red background'+Back.RESET )
    testA()
    
    
    

            
if __name__ == '__main__':
    main()

