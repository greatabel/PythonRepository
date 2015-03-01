from atexit import register
from random import randrange
from threading import BoundedSemaphore,Lock,Thread,currentThread
from time import sleep,ctime

lock=Lock()
MAX=5
candytray=BoundedSemaphore(MAX)

def refill():
 lock.acquire()
 print 'Refiling candy..'
 try:
  candytray.release()
 except ValueError:
  print 'full,skipping'
 else:
  print 'OK'
 lock.release()

def buy():
 lock.acquire()
 print 'Buying candy..'
 if candytray.acquire(False):
   print 'buy OK'
 else:
   print 'empty'
 lock.release()


def producer(loops):
 for i in xrange(loops):
  refill()
  sleep(randrange(3))
 
def consumer(loops):
 for i in xrange(loops):
  buy()
  myname=currentThread().name
  print 'time:[%s] Started threadname:%s' %(ctime(),myname)
  sleep(randrange(3))

def _main():
    print 'starting at:', ctime()
    
    print randrange(3)
    nloops = randrange(2, 6)
    print 'THE CANDY MACHINE (full with %d bars)!' % MAX
    Thread(target=consumer, args=(randrange(
        nloops, nloops+MAX+2),)).start() # buyer
    Thread(target=producer, args=(nloops,)).start() # vendor

@register
def _atexit():
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    _main()
