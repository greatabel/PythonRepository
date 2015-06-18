
from collections import OrderedDict

import colorama
from colorama import Fore, Back, Style

a = [1,10,2,20,3,30,2,2,20]
b = [1,10,2,20,3,30,2,2,20]
c=[{'x':1,'y':2},{'x':1,'y':20},{'x':1000,'y':2000},{'x':1,'y':2},{'x':1,'y':2}]
def myway():
    print(a,'len(a)',len(a))
    myset = set()
    rmLen = 0

    for i in range(len(a)):
        if a[i] not in myset:
            myset.add(a[i])
            print(i,'add',a[i])
        else:
            print(i,"remove",a[i])
            # rmLen += 1
            a[i] = '#'
            # del a[i]
    print(a)
    x = list(filter(lambda x:x!='#',a))
    
    print(x)


def deduplicate(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def deduplicateCanHandleUnhashableType(items ,key=None):
    seen = set()
    for item in items:

        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

def betterWay():
    print(list(deduplicate(b)))
    print("before",c)
    print(list(deduplicateCanHandleUnhashableType(c, key=lambda d:(d['x'],d['y']) )))
    print(list(deduplicateCanHandleUnhashableType(c, key=lambda d:(d['x']) )))

def main():
    colorama.init()
    text='test'
    print(Fore.RED + "my way" + Style.RESET_ALL)
    myway()
    print(Fore.BLUE + "better way" + Style.RESET_ALL)
    betterWay()


if __name__ == '__main__':
    main()