from collections import OrderedDict

import colorama
from colorama import Fore, Back, Style

from datetime import timedelta, datetime,date
import calendar



def main():
    text = '2015-01-01'
    y = datetime.strptime(text,'%Y-%m-%d')
    z = datetime.now()
    print(y,z)
    diff =  z - y
    print(diff)

    print(Fore.GREEN + "more accurate" + Style.RESET_ALL)
    

    
    



if __name__ == '__main__':
    main()
