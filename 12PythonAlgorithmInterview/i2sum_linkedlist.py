'''

给定2个单链表 链表每个节点代表1位数，计算2个数之和。例如：
输入(3->1->5) 和 （5->9->2)，输出 8->0->8，即是513 + 295 = 808
注意个位数在链表头

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





