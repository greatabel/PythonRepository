'''

如何对链表进行重新排序
L0 -> L1 -> L2 ... -> Ln-1 -> Ln-1
重新排列为：
L0 -> Ln -> L1 -> Ln-1 ->L2 -> Ln-2 ...

要求：1. 在原来链表基础上进行排序，即不能申请新节点
     2. 只能修改节点的next域，不能修改数据域

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





