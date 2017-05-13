from collections import OrderedDict

import colorama
from colorama import Fore, Back, Style

from datetime import datetime
from pytz import timezone
import pytz



def main():
    d = datetime(2015,6,22,0,0,0)
    print(d)

    center = timezone('US/Central')
    local_d = center.localize(d)
    print(local_d)
    center = timezone('Asia/Shanghai')
    local_d = center.localize(d)
    print(local_d)

    print(pytz.country_timezones('IN'))

    print(Fore.GREEN + "more accurate" + Style.RESET_ALL)
    

    
    



if __name__ == '__main__':
    main()
