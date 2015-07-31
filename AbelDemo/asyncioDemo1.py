#http://www.giantflyingsaucer.com/blog/?p=5557
import asyncio

@asyncio.coroutine
def my_coroutine(task_name, seconds_to_sleep=3):
    print("{0} sleeping for: {1} seconds".format(task_name, seconds_to_sleep))
    yield from asyncio.sleep(seconds_to_sleep)
    print("{0} finished".format(task_name))

def main():
    loop = asyncio.get_event_loop()
    tasks = [
    my_coroutine('task1',4),
    my_coroutine('task2',2),
    my_coroutine('task3',3)

    ]
    loop.run_until_complete(
        asyncio.wait(tasks)
        )
    loop.close()
    

    
    



if __name__ == '__main__':
    main()

