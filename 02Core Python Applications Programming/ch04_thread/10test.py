from atexit import register
from random import randrange
from threading import Thread,Lock,currentThread
from time import sleep,ctime

class CleanOutputSet(set):
 def __str__(self):
  return '-^-'.join(x for x in self)

lock=Lock()
loops=(randrange(10,13) for x in xrange(randrange(3,7)))

for i in loops:
 print 'in loops=',i
loops=(randrange(10,13) for x in xrange(randrange(3,7)))
for i in loops:
 print '1>in loops=',i
loops=(randrange(10,13) for x in xrange(randrange(3,7)))
for i in loops:
 print '2>in loops=',i
loops=(randrange(10,13) for x in xrange(randrange(3,7)))
remaining=CleanOutputSet()

def loop(nsec):
 myname=currentThread().name
 lock.acquire()
 remaining.add(myname)
 print 'time:[%s] Started threadname:%s' %(ctime(),myname)
 lock.release()
 sleep(nsec)
 lock.acquire()
 remaining.remove(myname)
 print 'time:[%s] Completed %s(%d seconds)' %(ctime(),myname,nsec)
 print ' (remaining %s)' %(remaining or 'None')
 lock.release()

def _main():
 for pause in loops:
  Thread(target=loop,args=(pause,)).start()

@register
def _atexit():
 print 'all done at:',ctime()

if __name__ =='__main__':
 _main()
 
