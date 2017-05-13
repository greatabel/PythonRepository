from collections import OrderedDict

import colorama
from colorama import Fore, Back, Style

from datetime import timedelta, datetime,date
import calendar



def main():
    with open('passwd.txt') as f:
        try:
            while True:
                line = next(f)
                if line is None:
                    break
                print(line, end='')
        except StopIteration:
            pass
            
if __name__ == '__main__':
    main()

