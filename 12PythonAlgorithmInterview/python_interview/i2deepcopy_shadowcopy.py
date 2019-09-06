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

    print(colored('--------------------', 'green'), '相关复习', colored('-'*20, 'red'))
    print('可变对象：list,dict, set 不可变对象：tuple,string int float bool', )
    #  可变对象
    a = [1, 2, 3]
    print(a)
    a[1] = 20
    print(a)
    b = (1, 2, 3)
    try:
        b[1] = 200
    except:
        print('修改不可修改对象失败') 



if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





