from queue import Queue
from threading import Thread
import time

def producer(out_q):
    n = 10
    while n > 0:
        out_q.put(n)
        time.sleep(2)
        n -= 1

        out_q.put(_sentinel)


def consumer(in_q):
    while True:

        data = in_q.get()

        if data is _sentinel:
            in_q.put(_sentinel)
            break

        print('Got:', data)

    print('consumer shutting down')

if __name__ == '__main__':
    q = Queue()
    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=producer, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
