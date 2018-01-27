from multiprocessing import Process, Queue
from termcolor import colored

def f(q):
    q.put([42, None, 'hello'])
    show = colored("q.put([42, None, 'hello'])", "red", attrs=['reverse', 'blink'])
    print(show)

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print('in main q.get()=', q.get())    # prints "[42, None, 'hello']"
    p.join()