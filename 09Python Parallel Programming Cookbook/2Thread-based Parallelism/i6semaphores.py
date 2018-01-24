import threading
import time
import random

semaphore = threading.Semaphore(0)

def consumer():
    print("consumer is waiting")

def producer():
    global item
    time.sleep(1.5)
    item = random.randint(0, 100)
    print ("producer notify : producted item number %s" %item)

if __name__ == '__main__':
    for i in range (5):
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    print ("main program terminated")