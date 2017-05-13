from queue import Queue
from threading import Thread
import time


# A thread that produces data
def producer(out_q):
    n = 10
    while n > 0:
        # Produce some data
        out_q.put(n)
        time.sleep(0.2)
        n -= 1


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        # Process the data
        print('Got:', data)
        if data <= 1:
            break

    print('Consumer shutting down')

if __name__ == '__main__':
    q = Queue()
    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=producer, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

