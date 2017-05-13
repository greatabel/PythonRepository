#https://pypi.python.org/pypi/colorama

from colorama import Fore, Back, Style




def main():
    print(Back.GREEN + 'my way'+Back.RESET )
    
    a = [1, 2, 3]
    b = ['u','v','w', 'x', 'y', 'z']
    from itertools import chain
    for x in chain(a,b):
        print(x)


    
    
    

            
if __name__ == '__main__':
    main()

