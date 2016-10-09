#http://www.giantflyingsaucer.com/blog/?p=5557
import asyncio

@asyncio.coroutine
def my_coroutine(future,task_name, seconds_to_sleep=3):
    print("{0} sleeping for: {1} seconds".format(task_name, seconds_to_sleep))
    yield from asyncio.sleep(seconds_to_sleep)
    #https://docs.python.org/3/library/asyncio-task.html#asyncio.Future.set_result
    future.set_result("{0} finished".format(task_name))

def got_result(future):
    print(future.result())


def main():
    loop = asyncio.get_event_loop()
    future1 = asyncio.Future()
    future2 = asyncio.Future()

    tasks = [
    my_coroutine(future1,'task1',4),
    my_coroutine(future2,'task2',2)


    ]
    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    loop.run_until_complete(
        asyncio.wait(tasks)
        )
    loop.close()
    

    
    



if __name__ == '__main__':
    main()


