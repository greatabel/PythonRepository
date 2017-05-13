from threading import Thread
import time


class CountdownThread(Thread): 
    def __init__(self, n):
        # print('n=',n)
        super().__init__()
        self.n = n

    def run(self):
        while self.n > 0:
            print('T-minus', self.n) 
            self.n -= 1 
            time.sleep(0.5)

# print('main')
c = CountdownThread(5)
c.start()

