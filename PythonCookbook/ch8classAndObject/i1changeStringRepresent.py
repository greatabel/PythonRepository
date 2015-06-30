#encoding:utf-8
from colorama import Fore, Back, Style

class Pair:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s},{0.y!s})'.format(self)


def main():
    p = Pair(10, 90)
#     Type "help", "copyright", "credits" or "license" for more information.
# >>> import i1changeStringRepresent
# >>> i1changeStringRepresent.Pair(3,4)
    print(p)

    print(Fore.BLUE + "other way:" + Style.RESET_ALL)
   
    


    print(Back.GREEN + 'demo2'+ Back.RESET)






            
if __name__ == '__main__':
    main()

