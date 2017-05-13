# http://www.cnblogs.com/ifantastic/p/3175735.html
# http://www.zlovezl.cn/articles/__init__-and__new__-in-python/
class Foo(object):
    def __init__(self, *args, **kwargs):
        print('in __init__ in Foo')

    def __new__(cls, *args, **kwargs):
        return object.__new__(Stranger, *args, **kwargs)

class Stranger(object):
    """docstring for Stranger"""
    def __init__(self, arg):
        print('in Stranger __init__')

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name,self.age,'#')



class PositiveInteger(int):
    def __new__(cls, value):
        return super(PositiveInteger, cls).__new__(cls, abs(value))

class Singleton(object):
    def __new__(cls):
        # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance



if __name__ == "__main__":
    foo = Foo()
    print(type(foo))
    s = Stranger("abel", 28)

    i = PositiveInteger(-3)
    print(i)

    obj1 = Singleton()
    obj2 = Singleton()

    obj1.attr1 = 'value1'
    print(obj1.attr1, obj2.attr1)
    print(obj1 is obj2)
        