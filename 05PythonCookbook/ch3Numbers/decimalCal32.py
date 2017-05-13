from collections import OrderedDict

import colorama
from colorama import Fore, Back, Style



def main():
    from decimal import Decimal,localcontext
    a = 4.2
    b = 2.1
    c = a + b
    print(c,round(c,2))
    print(Fore.GREEN + "more accurate" + Style.RESET_ALL)
    a = Decimal('4.2')
    b = Decimal('2.1')
    print(a+b)

    a = Decimal('1.3')
    b = Decimal('1.7')
    print(a/b)
    with localcontext() as ctx:
        ctx.prec = 3
        print(a/b)




if __name__ == '__main__':
    main()
