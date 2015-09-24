from threading import Thread
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
            time.sleep(3)

if __name__ == "__main__":
    c = CountdownTask()
    t = Thread(target=c.run, args=(10,))
    t.start()

    time.sleep(20)
    print('About to terminate')
    c.terminate()
    t.join()
    print('Terminated')