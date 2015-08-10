from functools import wraps

class A:

    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decorator1')
            return func(*args, **kwargs)
        return wrapper

    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decorator2')
            return func(*args, **kwargs)
        return wrapper

a = A()

@a.decorator1
def spam():
    pass

@A.decorator2
def grok():
    pass

spam()
grok()