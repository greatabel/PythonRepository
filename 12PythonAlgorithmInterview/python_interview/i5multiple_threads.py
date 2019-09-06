'''

Python中如何实现多线程？

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





