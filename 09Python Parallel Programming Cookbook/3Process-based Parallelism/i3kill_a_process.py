import multiprocessing
import time


def foo():
    print ('Starting function')
    time.sleep(0.1)
    print ('Finished function')

if __name__ == '__main__':
    p  = multiprocessing.Process\
                         (name='i0',\
                          target=foo)
    print ('Process before execution:', p, p.is_alive())

    p.start()
    print ('Process running:', p, p.is_alive())

    p.terminate()
    print ('Process terminated:', p, p.is_alive())
    time.sleep(0.2)
    print ('After 0.2s, Process terminated:', p, p.is_alive())

    p.join()
    print ('Process joined:', p, p.is_alive())

    print ('Process exit code:', p.exitcode)

