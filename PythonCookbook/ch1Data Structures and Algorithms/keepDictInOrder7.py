
from collections import OrderedDict

import colorama
from colorama import Fore, Back, Style



def main():
    colorama.init()
    text='test'
    print(Fore.RED + text)
    print(Back.GREEN + text + Style.RESET_ALL)
    d = OrderedDict()
    d['test1'] = 1
    d['test2'] = 2
    d['test30'] = 30
    print(d)

    import json
    print(json.dumps(d))


if __name__ == '__main__':
    main()