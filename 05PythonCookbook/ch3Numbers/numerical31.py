from collections import OrderedDict

import colorama
from colorama import Fore, Back, Style



def main():
    print(round(1.2333,1))
    print(round(1.27, 1))
    print(round(-1.27, 1))
    a = 1627731
    print('he number of digits given to round() can be negative, '+
        'in which case rounding takes place for tens, hundreds, thousands,')
    print(round(a, -1))   
    print(round(a, -2))   
    print(round(a, -3))
    #just print
    print(format(1.234,'0.2f'))   
    print(format(1.234,'0.3f'))
    print('vale is {:0.3f}'.format(1.234))   

    a = 2.1
    b = 4.2
    c = a + b
    print(c,round(c,2))

if __name__ == '__main__':
    main()
