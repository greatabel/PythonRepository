from functools import wraps
import inspect

def optional_debug(func): 

    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs): 
        if debug:
            print('Calling', func.__name__) 
        return func(*args, **kwargs)

    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter('debug',
                                       inspect.Parameter.KEYWORD_ONLY,
                                       default=False))

    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper

@optional_debug
def spam(a,b,c):
    print(a,b,c,"in spam")

if __name__ == "__main__":
    spam(1,2,3)
    spam(1,2,3,debug=True)

    print('但是debug 参数还是不在函数的参数查询中')
    def add(x, y):
        return x + y

    print(inspect.signature(add))

    @optional_debug
    def add_A(x, y):
        return x + y

    print(inspect.signature(add_A))