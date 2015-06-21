from collections import OrderedDict

import colorama
from colorama import Fore, Back, Style



def main():
    from decimal import Decimal
    a = 4.2
    b = 2.1
    c = a + b
    print(c,round(c,2))
    print(Fore.GREEN + "more accurate" + Style.RESET_ALL)
    a = Decimal('4.2')
    b = Decimal('2.1')
    print(a+b)



if __name__ == '__main__':
    main()
