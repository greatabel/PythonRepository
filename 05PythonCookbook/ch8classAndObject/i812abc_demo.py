from abc import ABCMeta
#https://docs.python.org/3.4/library/abc.html
class MyABC(metaclass=ABCMeta):
    pass

MyABC.register(tuple)



from abc import ABCMeta, abstractmethod

class abstractA(metaclass=ABCMeta):
    @abstractmethod
    def absMeth(self):
        pass
 
class A(abstractA):
    # must implement abstract method
    def absMeth(self):
        return 0


test = A()
print('t=',test.absMeth())

assert issubclass(tuple, MyABC) 
assert isinstance((), MyABC)
assert isinstance([1,2], MyABC)
#http://www.oschina.net/translate/when-to-use-assert
assert 1>0
assert 1>2




