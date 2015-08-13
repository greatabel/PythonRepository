import time
from functools import wraps

def timethis(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end-start,"in timethis")
        return r

    return wrapper


class Spam:
    @timethis
    def instance_method(self,n):
        print(self, n,"in instance_method")
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls,n):
        print(cls, n, "in class_method")
        while  n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n, "static_method")
        while n > 0:
            n -= 1

if __name__ == "__main__":
    s = Spam()
    s.instance_method(1000)
    Spam.class_method(10000)
    Spam.static_method(100000)