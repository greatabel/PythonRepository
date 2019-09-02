'''

给定2个单链表 链表每个节点代表1位数，计算2个数之和。例如：
输入(3->1->5) 和 （5->9->2)，输出 8->0->8，即是513 + 295 = 808
注意个位数在链表头

#----------------------------#

思路1: 最简单：先求出每个链表代表的整数，然后相加，缺点是：当链表代表数很大，就不行了
思路2: 对链表节点直接进行相加操作，然后相加的和存储到新链表对应节点，同时记录相加的进位

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





