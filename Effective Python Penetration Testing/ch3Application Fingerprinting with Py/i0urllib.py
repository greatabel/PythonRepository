import urllib.request

target_url = 'https://www.douban.com/'
with urllib.request.urlopen(target_url) as url:
    s = url.read()

print(s)
