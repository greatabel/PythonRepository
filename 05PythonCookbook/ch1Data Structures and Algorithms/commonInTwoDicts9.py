
from collections import OrderedDict

import colorama
from colorama import Fore, Back, Style

a = {
    'x':1,
    'y':2,
    'z':3
    }
b = {
    'x':11,
    'y':2,
    'w':3
    }

def myway():
    commonDicts = {}
    for key in a:
        if key in b.keys():
            if a[key] == b[key]:
                commonDicts[key]= a[key]
    print(commonDicts)

def betterWay():
    print("公共key",a.keys() & b.keys())
    print("在a不在b", a.keys() - b.keys())
    print("找公共的键值对",a.items()&b.items())
    #还可以构建特定的字典
    c = { key:a[key] for key in a.keys() - {'z','w'}}
    print("c=",c)

def main():
    colorama.init()
    text='test'
    print(Fore.RED + "my way" + Style.RESET_ALL)
    myway()
    print(Fore.BLUE + "better way" + Style.RESET_ALL)
    betterWay()


if __name__ == '__main__':
    main()