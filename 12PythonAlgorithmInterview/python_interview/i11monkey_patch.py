'''



#----------------------------#



'''

import time
from termcolor import colored


def main_process():
    t = '''
    Q 11. 什么是猴子补丁？
    在运行期间动态修改一个类或模块
    '''
    print(colored('-'*10, 'red'), t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





