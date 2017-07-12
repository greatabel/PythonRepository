import urllib.request
import urllib.parse

fields = {
    'name' : 'Sean',
    'email' : 'Sean@example.com'
}

parms = urllib.parse.urlencode(fields)
parms = parms.encode('utf8')
target_url = 'https://www.douban.com/'
with urllib.request.urlopen(target_url, parms) as url:
    s = url.read()
print(s)
