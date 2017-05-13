#encoding:utf-8
from colorama import Fore, Back, Style

class lazyproperty:
    def __init__(self, func):
        self.func = func
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


def main():
    
    c = Circle(4.0)
    print('redis=',c.radius)
    print(c.area)

    print(Fore.RED + "---:" + Style.RESET_ALL)
   
    


    print(Back.GREEN + '---'+ Back.RESET)






            
if __name__ == '__main__':
    main()

