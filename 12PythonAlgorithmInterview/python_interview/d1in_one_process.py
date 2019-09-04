'''

https://zhuanlan.zhihu.com/p/46368084

#----------------------------#



'''

import time
from termcolor import colored
import os


def long_time_task():
    print('当前进程: {}'.format(os.getpid()))
    time.sleep(3)
    print("结果: {}".format(8**20))


def main_process():
    print('当前母进程：{}'.format(os.getpid()))
    for i in range(2):
        long_time_task()

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





