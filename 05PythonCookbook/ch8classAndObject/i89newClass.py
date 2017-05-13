#encoding:utf-8
from colorama import Fore, Back, Style

class Integer:
    def __init__(self, name):
            self.name = name
    def __get__(self, instance, cls): 
        if instance is None:
            return self 
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value): 
        if not isinstance(value, int):
            raise TypeError('Expected an int') 
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

class Point:
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x, y):
            self.x = x
            self.y = y
    def __str__(self):
        return '({0.x!s},{0.y!s})'.format(self)
def main():
    p = Point(2, 10)
    print(p)
    p.x = 100
    print(p)
    print(Fore.RED + "---:" + Style.RESET_ALL)
    p.x = 100.1
   
    


    print(Back.GREEN + '---'+ Back.RESET)






            
if __name__ == '__main__':
    main()

