# http://stackoverflow.com/questions/5929107/python-decorators-with-parameters
class MyDec(object):
    def __init__(self,flag):
        self.flag = flag
    def __call__(self, original_func):
        decorator_self = self
        def wrappee( *args, **kwargs):
            print('in decorator before wrapee with flag ',decorator_self.flag)
            original_func(*args,**kwargs)
            print('in decorator after wrapee with flag ',decorator_self.flag)
        return wrappee

@MyDec('foo de fa fa')
def bar(a,b,c):
    print('in bar',a,b,c)




class decoratorWithoutArguments(object):

    def __init__(self, f):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        print("Inside __init__()")
        self.f = f

    def __call__(self, *args):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        print( "Inside __call__()")
        self.f(*args)
        print( "After self.f(*args)")

@decoratorWithoutArguments
def sayHello(a1, a2, a3, a4):
    print( 'sayHello arguments:', a1, a2, a3, a4)


class decoratorWithArguments(object):

    def __init__(self, arg1, arg2, arg3):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print( "Inside __init__()")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print( "Inside __call__()")
        def wrapped_f(*args):
            print( "Inside wrapped_f()")
            print( "Decorator arguments:", self.arg1, self.arg2, self.arg3)
            f(*args)
            print( "After f(*args)")
        return wrapped_f

@decoratorWithArguments("hello", "world", 42)
def sayHelloA(a1, a2, a3, a4):
    print( 'sayHello arguments:', a1, a2, a3, a4)

if __name__ == "__main__":
    bar('x','y','z')
    print('-'*10)
    sayHello("say", "hello", "argument", "list")
    print('-'*10)
    sayHelloA("say", "hello", "argument", "list")
