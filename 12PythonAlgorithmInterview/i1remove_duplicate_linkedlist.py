'''

1.2 给定一个没有排序的连标，去掉重复项，并保留顺序
例如1->3->1->5->5->7
变成1->3->5->7

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





