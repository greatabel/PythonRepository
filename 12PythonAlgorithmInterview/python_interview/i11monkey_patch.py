'''



#----------------------------#



'''

import time
from termcolor import colored


class A:
    def func(self):
        print('Hi')

    def monkey(self):
        print('Hi monkey!')


def main_process():
    t = '''
    Q 11. 什么是猴子补丁？
    在运行期间动态修改一个类或模块
    '''
    print(colored('-'*10, 'red'), t)

    a = A()
    a.func()
    print('使用猴子补丁')
    A.func = A.monkey
    a.func()
    print('其实这根本的原因在于Python语法的灵活性，方法可以像普通对象那样使用!')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





