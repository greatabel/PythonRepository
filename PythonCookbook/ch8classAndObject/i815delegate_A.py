class A:
    def spam(self,x):
        print('A.spam',x)

    def foo(self):
        print('A.foo')

class B(object):
    def __init__(self):
        self._a = A()

    

    def bar(self):
        print('B.bar')

    def __getattr__(self,name):
        return getattr(self._a, name)
    
if __name__ == '__main__':
    b = B()
    b.bar()
    b.spam(42)
    b.foo()