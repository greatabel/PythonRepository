'''



#----------------------------#



'''

import time
from termcolor import colored


def main_process():
    t = '''
    q: Python中是如何管理内存的?
    ans: Python有一个私有堆空间来保存所有的对象和数据结构。
    作为开发者，我们无法访问它，是解释器在管理它。但是有了核心API后，我们可以访问一些工具。
    Python内存管理器控制内存分配。

    另外，内置垃圾回收器会回收使用所有的未使用内存，所以使其适用于堆空间。
    '''
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





