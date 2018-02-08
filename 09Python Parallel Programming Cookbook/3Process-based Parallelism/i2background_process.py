import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print ("Starting %s \n" %name)
    time.sleep(1)
    file = open(name + ".txt", "w") 
    print ("Exiting %s \n" %name)

if __name__ == '__main__':
    background_process = multiprocessing.Process\
                         (name='0background_process', \
                          target=foo)
    background_process.daemon = True

    NO_background_process = multiprocessing.Process\
                            (name='0NO_background_process0',\
                             target=foo)    
    NO_background_process.daemon = False

    background_process.start()
    NO_background_process.start()
    time.sleep(3)
    print('主进程退出会杀死所有daemo进程，所以我迟一点!')