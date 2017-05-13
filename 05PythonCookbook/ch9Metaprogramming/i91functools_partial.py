# http://blog.jkey.lu/2013/03/15/python-decorator-and-functools-module/
#
# 我们知道 python 中有个 int([x[,base]]) 函数，作用是把字符串转换为一个普通的整型。
# 如果要把所有输入的二进制数转为整型，那么就要这样写 int('11', base=2)。
# 这样写起来貌似不太方便，那么我们就能用 partial 来实现值传递一个参数就能转换二进制数转为整型的方法
#
from functools import partial
int2 = partial(int, base=2)




from functools import wraps
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('#calling decorated function')
        return f(*args, **kwds)
        
    return wrapper

@my_decorator
def example():
    print("Calling example func")

if __name__ == "__main__":
    print(int2('11'))
    print(int2('101'))

    example()