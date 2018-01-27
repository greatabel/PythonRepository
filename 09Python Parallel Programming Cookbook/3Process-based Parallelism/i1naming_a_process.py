import multiprocessing
import time
from termcolor import colored


def foo():
    name = multiprocessing.current_process().name
    show = colored(("Starting %s \n" %name), "red", attrs=['reverse', 'blink'])
    print (show)
    time.sleep(3)
    print ("Exiting %s \n" %name)

if __name__ == '__main__':
    print('Main#')
    process_with_name = \
                      multiprocessing.Process\
                      (name='1foo_process',\
                       target=foo)
    # process_with_name.daemon = True
    process_with_default_name = \
                              multiprocessing.Process\
                              (target=foo)
    process_with_name.start()
    process_with_default_name.start()
    print('Main exit#')