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

class Person:
    first_name = property()
    @first_name.getter
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._first_name = value

p = Person()
p.first_name = 'Dave'
print(p.first_name)
