import time

def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(0.5)

from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()

# You can query a thread instance to see if it’s still running:
if t.is_alive(): 
    print('Still running')
else: 
    print('Completed')
# You can also request to join with a thread, which waits for it to terminate:
t.join()
if t.is_alive(): 
    print('Still running')
else: 
    print('Completed')