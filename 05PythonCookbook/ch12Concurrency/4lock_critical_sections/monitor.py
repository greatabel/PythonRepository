import threading
import time

class SharedCounter: 
    '''
    A counter object that can be shared by multiple threads. 
    '''
    _lock = threading.RLock()
    def __init__(self, initial_value = 0):
        self._value = initial_value

    def incr(self,delta=1): 
        '''
    Increment the counter with locking 
        '''
        with SharedCounter._lock:
            self._value += delta
            if delta==1:
                print("+",self._value)
            else:
                print("-",self._value)

    def decr(self,delta=1): 
        '''
        Decrement the counter with locking 
        '''

        with SharedCounter._lock:
             self.incr(-delta)



def test(c):
    for n in range(10):
        time.sleep(0.2)
        c.incr()
    for n in range(10):
        time.sleep(0.1)
        c.decr()

if __name__ == '__main__' :
    c = SharedCounter()
    t1 = threading.Thread(target=test,args=(c,))
    t2 = threading.Thread(target=test,args=(c,))
    t3 = threading.Thread(target=test,args=(c,))
    t1.start()
    t2.start()
    t3.start()
    print('Running test')
    t1.join()
    t2.join()
    t3.join()

    assert c._value == 0
    print('Looks good!')