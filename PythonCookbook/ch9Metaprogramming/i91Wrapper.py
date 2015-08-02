import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper

if __name__ == "__main__":

    @timethis
    def countdown(n):
        while n > 0:
            n -= 1
    @timethis
    def countdownA(n,str):
        while n>0:
            n-=1
        print(str)

    countdown(10000)
    countdown(100000)
    countdownA(100000,'hello')