from time import sleep,ctime
import thread


def loop0():
				print '0'*10
				print 'start loop 0 at:',ctime()
				sleep(4)
				print 'loop 0 done at:',ctime()

def loop1():
    print '1'*10
    print 'start loop 1 at:', ctime()
    sleep(2)
    print 'loop 1 done at:', ctime()

def main():
    print 'starting at:',ctime()
    thread.start_new_thread(loop0,())
    thread.start_new_thread(loop1,())
    sleep(6)
    print 'all done at:',ctime()
    test(5)
    sleep(15)
    print 'main done'

def timer(i,internal):
   sleep(internal)
   ts='thread: '+str(i)+' - internal='+str(internal)
   print ts
   

def test(times):
  for i in range(times):
   print 'i in test=',i
   thread.start_new_thread(timer,(i,3*i))


if __name__ == '__main__':
  main()
