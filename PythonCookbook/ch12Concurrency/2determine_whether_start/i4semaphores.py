import threading
import time

def worker(n, sema):
    sema.acquire()

    print('Working', n)

sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n,sema,))
    t.daemon=True
    t.start()

if __name__ == "__main__":
    print('About to release first worker')
    time.sleep(0.5)
    sema.release()
    time.sleep(1)
    print('About to release second worker')
    time.sleep(0.5)
    sema.release()
    time.sleep(1)
    print('Goodbye')