'''

Q 2：深拷贝和浅拷贝之间的区别是什么？

#----------------------------#



'''

import time
from termcolor import colored


def main_process():
    print('Q 2：深拷贝和浅拷贝之间的区别是什么？')
    ans = '深拷贝就是将一个对象拷贝到另一个对象中，这意味着如果你对一个对象的拷贝做出改变时，不会影响原对象'
    print(colored('mycount=', 'red'), ans)

    print(colored('--------------------', 'green'), '可变对象/不可变对象', colored('-'*20, 'red'))
    print('可变对象：list,dict, set 不可变对象：tuple,string int float bool', )
    #  可变对象
    a = [1, 2, 3]
    print(a, 'id(a)=', id(a))
    a[1] = 20
    print(a, '修改后 id(a)=', id(a))
    print()
    b = (1, 2, 3)
    try:
        b[1] = 200
    except:
        print('修改不可修改对象失败') 

    b1 = b
    b = (4, 5, 6)
    print(b, b1, 'id(b),id(b1)=', id(b), id(b1))
    print(colored('--------------------', 'green'), '可变对象/不可变对象 作为函数参数',
             colored('-'*20, 'red'))
    def myfunc(l):
        l.append(1)
    l = [1, 2, 3]
    print('可变对象 作为函数参数', l)
    myfunc(l)
    print('可变对象 作为函数参数', l)

    def myfunc_unchangeable_para(a):
        a += 1
        print('in func', a)
    a = 2
    print('不可变对象，作为函数参数', a)
    myfunc_unchangeable_para(a)
    print('不可变对象，作为函数参数', a)
    print('结论：python中向函数传递参数只能是引用传递，表示把它的地址都传进去了，这才会带来上面的现象')




if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





