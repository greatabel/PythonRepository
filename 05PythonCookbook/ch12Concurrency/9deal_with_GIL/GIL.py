def  some_work(a,b,c):
    print("in some_work",a,b,c)
    return "some work"

def some_thread():
    while True:
        args =  (1,2,3)
        r = pool.apply(some_work, (args))

if __name__ == '__main__':
    import multiprocessing
    pool = multiprocessing.Pool()

    some_thread()
