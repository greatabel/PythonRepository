from collections import OrderedDict

import colorama
from colorama import Fore, Back, Style



def main():
    s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
     the eyes, not around the eyes, don't look around the eyes, look into my eyes, you're under."

    import textwrap
    print(textwrap.fill(s,70))
    print('-'*20)
    print(textwrap.fill(s,40))

if __name__ == '__main__':
    main()