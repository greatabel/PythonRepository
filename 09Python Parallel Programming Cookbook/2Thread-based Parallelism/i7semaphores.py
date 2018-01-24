# Semaphore（信号量）
# 在多线程编程中，为了防止不同的线程同时对一个公用的资源（比如全部变量）进行修改，
# 需要进行同时访问的数量（通常是1）。
# 信号量同步基于内部计数器，每调用一次acquire()，计数器减1；每调用一次release()，计数器加1.
# 当计数器为0时，acquire()调用被阻塞。
# http://www.dongwm.com/archives/%E4%BD%BF%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E5%B9%B6%E5%8F%91
# %E7%BC%96%E7%A8%8B-%E7%BA%BF%E7%A8%8B%E7%AF%87/

import time
from random import random
from threading import Thread, Semaphore

sema = Semaphore(3)

def foo(tid):
    with sema:
        print('tid<{}> acquire sema'.format(tid))
        wt = random() * 2
        # print('wt=', wt)
        time.sleep(wt)
    print('tid<{}> release sema'.format(tid))


def main():
    threads = []
    for i in range(5):
        t = Thread(target=foo, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()