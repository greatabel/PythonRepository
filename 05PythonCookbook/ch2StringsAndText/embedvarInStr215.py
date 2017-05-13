
from collections import OrderedDict

import colorama
from colorama import Fore, Back, Style

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

def main():
    s = '{name} has {n} message.'
    print(s.format(name="Test", n = 100))

    name = 'Gate'
    n = 22
    print(s.format_map(vars()))

    a = Info('Greatabel', 29)
    print(s.format_map(vars(a)))


if __name__ == '__main__':
    main()