import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start )
        return result
    return wrapper

@timethis
def countdown(n:int):
    while n > 0:
        n -= 1

if __name__ == "__main__":
    countdown(100000)
    print('Name:', countdown.__name__)
    print('Docstring:', repr(countdown.__doc__))
    print('Annotations:', countdown.__annotations__)