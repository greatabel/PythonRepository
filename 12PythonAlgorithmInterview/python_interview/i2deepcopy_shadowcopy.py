'''

Q 2：深拷贝和浅拷贝之间的区别是什么？

#----------------------------#



'''

import time
from termcolor import colored


def main_process():
    print('Q 2：深拷贝和浅拷贝之间的区别是什么？')
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





