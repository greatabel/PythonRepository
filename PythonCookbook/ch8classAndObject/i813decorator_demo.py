import colorama
from colorama import Fore, Back, Style
#http://www.cnblogs.com/Jerry-Chou/archive/2012/05/23/python-decorator-explain.html

def login():
    print('in login')

#---demo1
def printdebug(func):
    print('enter login #')
    func()
    print('exit login #')

#----demo2
def printdebug2(func):
    def __decorator():
            print('enter login #')
            func()
            print('exit login #')

    return __decorator

#----demo3
@printdebug2
def login2():
    print('in login2')

def main():
    print('-'*20,'demo1:')
    printdebug(login)

    print(Fore.GREEN + '-'*20 + Fore.RESET+Back.RED+'demo2'+Back.RESET)
    debug_login = printdebug2(login)
    debug_login()

    print(Fore.BLUE + '-'*20 + Fore.RESET+Back.RED+'demo2'+Back.RESET)
    login2()




if __name__ == '__main__':
    main()