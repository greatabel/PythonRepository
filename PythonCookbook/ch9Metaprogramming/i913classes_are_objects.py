def make_myklass(**kwattrs):
    return type("MyKlass",(object,), dict(**kwattrs))

myklass_foo_bar = make_myklass(foo=2,bar=4)
print(myklass_foo_bar)
x = myklass_foo_bar()
print('x.foo=',x.foo,x.bar)

print('等价于－》')

class MyKlass(object):
    foo = 2
    bar = 4

a = MyKlass()
print("a.foo=",a.foo,a.bar)

print('-'*20)
# http://pythoncentral.io/how-metaclasses-work-technically-in-python-2-and-3/
class a:
    def __init__(self, data):
        self.data = data
 
    def getd3(self):
        return self.data * 3
 
 
class MyMeta(type):
    def __new__(metaname, classname, baseclasses, attrs):
        print('New called with')
        print('metaname', metaname)
        print('classname', classname)
        print('baseclasses', baseclasses)
        print('attrs', attrs)
        attrs['getdata'] = a.__dict__['getd3']
        # attrs['getdata'] = a.getd3
        return type.__new__(metaname, classname, baseclasses, attrs)
 
    def __init__(classobject, classname, baseclasses, attrs):
        print('init called with')
        print('classobject', classobject)
        print('classname', classname)
        print('baseclasses', baseclasses)
        print('attrs', attrs)
 
 
class Kls(metaclass=MyMeta):
    def __init__(self,data):
        self.data = data
 
    def printd(self):
        print(self.data)
 
ik = Kls('arun')
ik.printd()
print(ik.getdata())