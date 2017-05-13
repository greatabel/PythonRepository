#encoding:utf-8
from colorama import Fore, Back, Style

def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)

from queue import Queue
from functools import wraps

class Async:
    def __init__(self, func, args):
                self.func = func
                self.args = args
                
def inlined_async(func):
    @wraps(func)
    def wrapper(*args): 
        f = func(*args)
        result_queue = Queue() 
        result_queue.put(None) 
        while True:
            result = result_queue.get() 
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put) 
            except StopIteration:
                break 
    return wrapper

def add(x, y): 

    return x + y

@inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello', 'world')) 
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r) 
    print('Goodbye')

def main():
    # Simple test
    print('# --- Simple test')
    test()

    print(Fore.BLUE + "other way:" + Style.RESET_ALL)
   
    print('# --- Multiprocessing test')
    import multiprocessing
    pool = multiprocessing.Pool()
    apply_async = pool.apply_async
    test()


    print(Back.GREEN + 'demo2'+ Back.RESET)






            
if __name__ == '__main__':
    main()
