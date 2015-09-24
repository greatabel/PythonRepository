from threading import Thread
import multiprocessing
import time

class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print("减去-", n)
            n -= 1
            time.sleep(0.3)

if __name__ == "__main__":
    c = CountdownTask()
    p = multiprocessing.Process(target=c.run,args=(10,))
    p.start()

    time.sleep(5)
    print('About to terminate')
    c.terminate()
 
    print('Terminated')