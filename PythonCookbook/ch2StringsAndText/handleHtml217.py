from collections import OrderedDict

import colorama
from colorama import Fore, Back, Style



def main():
    s = 'Elements are written as "<tag>text</tag>".'
    import html
    print(s)
    print(html.escape(s))

if __name__ == '__main__':
    main()