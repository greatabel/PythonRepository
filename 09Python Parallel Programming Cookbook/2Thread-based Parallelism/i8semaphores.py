import threading
import time
import logging
from random import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

class ThreadPool(object):
    def __init__(self):
        super(ThreadPool, self).__init__()
        self.activate = []
        self.lock = threading.Lock()

    def makeActivate(self, name):
        with self.lock:
            self.activate.append(name)
            logging.debug('Running: %s', self.activate)

    def makeInactivate(self, name):
        with self.lock:
            self.activate.remove(name)
            logging.debug('rm %s, Running: %s', name, self.activate)

def f(s, pool):
    logging.debug('Waiting to join the pool')
    with s:
        name = threading.currentThread().getName()
        pool.makeActivate(name)
        wt = random() * 2
        time.sleep(wt)
        pool.makeInactivate(name)

if __name__ == '__main__':
    pool = ThreadPool()
    s = threading.Semaphore(3)

    threads = []
    for i in range(10):
        t = threading.Thread(target=f, name='thread_'+str(i), args=(s, pool))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()