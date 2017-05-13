#encoding:utf-8
from colorama import Fore, Back, Style

def spam(a,b=42):
    print(a,'b=',b)


def main():
    add = lambda x, y : x + y
    print(add(1,9))
    print(add('Hello ','World'))
    print(Fore.BLUE + "other way:" + Style.RESET_ALL)
    names = ['David Beazley', 'Brian Jones','Raymond Hettinger', 'Ned Batchelder']
    sortednames = sorted(names, key=lambda name: name.split()[-1].lower())
    print(sortednames)
   
    


    print(Back.GREEN + 'demo2'+ Back.RESET)






            
if __name__ == '__main__':
    main()
