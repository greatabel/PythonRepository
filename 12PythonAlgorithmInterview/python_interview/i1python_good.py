'''



#----------------------------#



'''

import time
from termcolor import colored


def main_process():
    print('Python有哪些特点和优点？')
    lst = ['可解释', '动态性', '面向对象', '开源', '强大社区支持']
    print(colored(lst, 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





