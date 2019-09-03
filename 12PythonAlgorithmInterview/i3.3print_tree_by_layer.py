'''

给定一颗二叉树，要求逐层打印二叉树节点的数据，例如有如下二叉树：
     1
  2    3
 4 5  6 7

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





