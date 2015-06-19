
from collections import OrderedDict

import colorama
from colorama import Fore, Back, Style



def main():
    colorama.init()
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    import re
    print(re.split(r'[;,\s]\s*',line))


if __name__ == '__main__':
    main()