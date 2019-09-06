'''

列表和元组之间的区别是？

#----------------------------#



'''

import time
from termcolor import colored


def main_process():
    q = '列表和元组之间的区别是？'
    ans = '二者的主要区别是列表是可变的，而元组是不可变的'
    print(colored(q, 'red'), ans)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





