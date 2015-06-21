from collections import OrderedDict

import colorama
from colorama import Fore, Back, Style



def main():
    from datetime import timedelta
    a = timedelta(days=2,hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    print(a,b,c)
    print(c.days,c.seconds,c.seconds/3600)


    print(Fore.GREEN + "more accurate" + Style.RESET_ALL)

    from datetime import datetime
    a = datetime(2015,6,21)
    print(a+timedelta(days=10))
    b = datetime(2016,1,1)
    d = b - a
    print(d.days)
    



if __name__ == '__main__':
    main()
