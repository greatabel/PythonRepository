#http://www.giantflyingsaucer.com/blog/?p=5557
import asyncio
import aiohttp

@asyncio.coroutine
def fetch_page(url):
    response = yield from aiohttp.request('GET', url)
    assert response.status == 200
    content = yield from response.read()
    print('URL: {0}:  Content: {1}'.format(url, content[0:20]))



def main():
    loop = asyncio.get_event_loop()
    

    tasks = [
    fetch_page('http://www.baidu.com'),
    fetch_page('http://www.douban.com')


    ]
    

    loop.run_until_complete(
        asyncio.wait(tasks)
        )
    loop.close()

    for task in tasks:
        print(task)
    

    
    



if __name__ == '__main__':
    main()


