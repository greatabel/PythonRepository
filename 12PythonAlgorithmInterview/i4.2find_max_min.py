'''

给定数组a1,a2,...,an,找出最大值，最小值。假设数组中的值两两个不相同

#----------------------------#



'''

import time
from termcolor import colored


def find_max_min(arr):
    return max(arr), min(arr)

def main_process():
    array =[7,3,19,40,4,7,1]
    imax, imin = find_max_min(array)
    print(colored('mycount=', 'red'),imax, imin)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





