# http://thecodeship.com/patterns/guide-to-python-function-decorators/
def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

@p_decorate
def get_text(name):
    return "{0} here".format(name)

print( get_text("Abel"))

# http://www.cnblogs.com/Jerry-Chou/archive/2012/05/23/python-decorator-explain.html

def printdebug_level(level):  #add wrapper to recevie decorator's parameter
    def printdebug(func):
        def __decorator(user):    
            print('enter the login, and debug level is: ' + str(level)) #print debug level
            func(user)  
            print('exit the login')
        return __decorator  
    return printdebug    #return original decorator
 
@printdebug_level(level=5)   #decorator's parameter, debug level set to 5
def login(user):
    print('in login:' + user)
 
login('jatsz')

# http://blog.xiayf.cn/2013/01/04/Decorators-and-Functional-Python/ 

from functools import wraps

def argumentative_decorator(gift):

    def func_wrapper(func):
        @wraps(func)
        def returned_wrapper(*args, **kwargs):
            print("gift",gift)
            return func(gift, *args, **kwargs)
        return returned_wrapper

    return func_wrapper

@argumentative_decorator('test')
def grateful_function(giftA):
    print("giftA **:",giftA)

grateful_function()




print('--------------')



GLOBAL_NAME = "Brian"

def print_name(function=None, name=GLOBAL_NAME):
    print('@^@',function,name)
    def actual_decorator(function):
        @wraps(function)
        def returned_func(*args, **kwargs):
            print("My name is " + name)
            return function(*args, **kwargs)
        return returned_func


    if not function:    # User passed in a name argument
        def waiting_for_func(function):
            print('waiting_for_func-->',function)
            return actual_decorator(function)
        return waiting_for_func

    else:
        print('actual_decorator-->',function)
        return actual_decorator(function)

@print_name
def a_function():
    print("I like the name!")

@print_name(name='Matt')
def another_function():
    print("Hey, that's new!")

if __name__ == "__main__":
        a_function()
        # >> My name is Brian
        # >> I like that name!

        another_function()
        # >> My name is Matt
        # >> Hey, that's new!