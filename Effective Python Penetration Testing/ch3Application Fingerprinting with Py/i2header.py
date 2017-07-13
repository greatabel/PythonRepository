import urllib.request

target_url = 'https://www.douban.com/'
with urllib.request.urlopen(target_url) as url:
    response_header = url.info()
    # s = url.read()
    print('response_header=', response_header)
    server = response_header['server']
print(server)
