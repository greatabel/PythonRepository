import thread
from time import sleep,ctime

loops=[4,2,1,5]

def loop(nloop,nsec,lock):
  print '\nstart loop',nloop, 'at:', ctime()
  sleep(nsec)
  print '\nloop',nloop,' done at:',ctime()
  lock.release()

def main():
 print 'starting main...'
 locks=[]
 nloops=range(len(loops))
 
 for i in nloops:
  lock = thread.allocate_lock()
  lock.acquire()
  locks.append(lock)
 
 for i in nloops:
  thread.start_new_thread(loop,(i,loops[i],locks[i]))

 for i in nloops:
  while locks[i].locked():
   pass

 print 'main done',ctime()

if __name__ == '__main__':
  main()
