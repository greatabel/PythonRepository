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

if __name__ == '__main__':
    main()
