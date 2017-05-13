class A:
    def spam(self,x):
        print('A.spam',x)

    def foo(self):
        print('A.foo')

class B(object):
    def __init__(self):
        self._a = A()

    def spam(self,x):
        return self._a.spam(x)

    def foo(self):
        return self._a.foo()

    def bar(self):
        print('B.bar')
    
if __name__ == '__main__':
    b = B()
    b.bar()
    b.spam(42)
    b.foo()