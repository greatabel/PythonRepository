from threading import Thread

def run_thread(n):
    for i in range(n):
        print(i)

def test():
    t1 = Thread(target=run_thread, args=(5,))
    t1.start()

if __name__ == "__main__":
    test()