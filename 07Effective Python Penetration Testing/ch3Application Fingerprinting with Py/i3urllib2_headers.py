try:
    from urllib.request import Request, urlopen  # Python 3
except:
    from urllib2 import Request, urlopen  # Python 2


headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0'
}

target_url = 'https://www.douban.com/'

q = Request(target_url, headers=headers)

a = urlopen(q).read()

print(a)
