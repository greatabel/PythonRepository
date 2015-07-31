# http://blog.csdn.net/iamaiearner/article/details/9371315

import weakref

class TestObj:
    pass

#是在建立弱引用的时候指定一个回调函数，一旦自己引用的对象被销毁，将会调用这个回调函数
def test_func(reference):
    print("Hello from callback function!")
    if reference is not None:
        try:
            print(reference, "This weak reference is no longer valid")
        except Exception as e:
            print('error here: ',e)

class TestObjA:
    def __init__(self):
        self.test_attr = 100

if __name__ == "__main__":

    
    a = TestObj()
    #建立一个弱引用
    x = weakref.ref(a)
    print(x,'#\n',x())

    y = weakref.ref(a,test_func)
    del a

    aa = TestObjA()
    z = weakref.proxy(aa, test_func)
    print(aa.test_attr)
    print(z.test_attr)
    del aa
