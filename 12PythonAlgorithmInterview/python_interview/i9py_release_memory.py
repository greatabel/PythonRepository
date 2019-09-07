'''



#----------------------------#



'''

import time
from termcolor import colored


def main_process():
    t = '''
    q: 当退出Python时，是否释放全部内存？
    ans:答案是No。循环引用其它对象或引用自全局命名空间的对象的模块，在Python退出时并非完全释放。
    另外，也不会释放C库保留的内存部分
    '''
    print(colored('mycount=', 'red'), t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





