
from collections import OrderedDict

import colorama
from colorama import Fore, Back, Style



def main():
    colorama.init()
    a = {'x':1, 'z':3}
    b = {'x':1, 'y':2}
    from collections import ChainMap
    c = ChainMap(a,b)
    print(c['x'])
    print(c['y'])
    print(c['z'])


if __name__ == '__main__':
    main()