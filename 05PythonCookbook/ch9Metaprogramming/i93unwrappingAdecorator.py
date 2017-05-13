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
    print('in countdown')
    while n > 0:
        n -= 1

@timethis
def add(x, y):
        print('x,y:',x,y)
        return x + y

if __name__ == "__main__":
    countdown(100000)
    origin_countdown = countdown.__wrapped__
    origin_countdown(100)
    
    add(1,9)
    origin_add = add.__wrapped__
    print(origin_add(1,9))