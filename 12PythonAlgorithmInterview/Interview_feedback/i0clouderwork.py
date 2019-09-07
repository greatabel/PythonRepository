'''



#----------------------------#

https://juejin.im/entry/57bd4e6fa633bd005d482ed1


'''

import time
from termcolor import colored


def main_process():
    t = '''
    1. HTTP Methods 一共有九个，分别是 GET，HEAD，POST，PUT，DELETE，TRACE，OPTIONS，CONNECT，PATCH。
    在RESTful API 设计中，常用的有POST，GET，PUT，PATCH 和 DELETE

    2. 

    '''
    print(colored('-'*20, 'red'), t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





