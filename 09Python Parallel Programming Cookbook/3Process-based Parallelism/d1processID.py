from multiprocessing import Process
import os
from termcolor import colored

def info(title):
    print(title)
    print('module name:', __name__)
    if hasattr(os, 'getppid'):  # only available on Unix
        print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('function f')
    print('#'*10, 'hello', name)

if __name__ == '__main__':

    show = colored("here#", "red", attrs=['reverse', 'blink'])
    print(show)
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
