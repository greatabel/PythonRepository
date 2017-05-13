import os

def child():
    import time
    time.sleep(3)
    print('*'*20)
    print('\nin child() # A new child ', os.getpid())
    os._exit(0)

def parent():
    while True:
        print('-'*10,'#','-'*10)
        newpid = os.fork()
        print("in parent() newpid=", newpid)
        if newpid == 0:
            child()
        else:
            pids = (os.getpid(), newpid)
            # print("pids=", pids)
            print("parent: %d, child: %d\n" % pids)
        reply = input("q for quit / c for new fork\n")

        if reply == 'c':
            print("reply=", reply)
            continue
        else:
            break

if __name__ == "__main__":
    parent()