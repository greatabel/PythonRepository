'''

设计一个程序，当输入一个字符串，输出所有排列
例如abc，输出：a,b,c所有的pailie:abc,acb,bac,bca,cba,cab

#----------------------------#



'''

import time
from termcolor import colored


def main_process():
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





