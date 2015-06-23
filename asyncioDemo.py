#http://www.giantflyingsaucer.com/blog/?p=5557
import asyncio

@asyncio.coroutine
def my_coroutine(seconds_to_sleep=3):
    print("my coroutine sleeping for: {0} seconds".format(seconds_to_sleep))
    yield from asyncio.sleep(seconds_to_sleep)

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.gather(my_coroutine()))
    loop.close()
    

    
    



if __name__ == '__main__':
    main()
