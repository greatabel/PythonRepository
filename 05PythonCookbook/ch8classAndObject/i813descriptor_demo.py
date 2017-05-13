import colorama
from colorama import Fore, Back, Style

#http://www.geekfan.net/7862/
class Movie(object):
    def __init__(self, title, rating, runtime, budget, gross):
        self.title = title
        self.rating = rating
        self.runtime = runtime
        # if budget < 0:
        #     raise ValueError("Negative not allowed :%s" % budget )
        self.budget = budget
        self.gross = gross

    @property
    def budget(self):
        return self._budget
    
    @budget.setter
    def budget(self,value):
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._budget = value

    @property
    def rating(self):
        return self._rating
 
    @rating.setter
    def rating(self, value):
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._rating = value

    def profit(self):
        return self.gross - self.budget

#------better way:
from weakref import WeakKeyDictionary

class NonNegative(object):
    """docstring for NonNegative"""
    def __init__(self, default):
        self.default = default
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.data.get(instance,self.default)

    def __set__(self,instance, value):
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self.data[instance] = value

class MoiveNew(object):
   
   #always put descriptor at class-level
    rating = NonNegative(0)
    runtime = NonNegative(0)
    budget = NonNegative(0)
    gross = NonNegative(0)

    def __init__(self, title, rating, runtime, budget, gross):
        self.title = title
        self.rating = rating
        self.runtime = runtime
        self.budget = budget
        self.gross = gross

    def profit(self):
        return self.gross - self.budget
        
        

def main():
    print('-'*20,'demo1:')
    m = Movie("Terminator", 5, 111, 20, 50)
    print(m.profit())
    m.budget = 40
    print(m.profit())
    try:
        m.budget = -100
        m.rating = -2
    except ValueError:
        print("ValueError here")


    print(Fore.GREEN + '-'*20 + Fore.RESET+Back.RED+'demo2'+Back.RESET)
    n = MoiveNew('Casablanca', 97, 102, 964000, 1300000)
    print(m.budget)
    m.rating = 100
    try:
        m.rating = -1
    except ValueError:
        print("here ValueError")





if __name__ == '__main__':
    main()