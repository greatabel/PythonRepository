# try:
#     from urllib.request import Request, urlopen  # Python 3
#     import urllib.build_opener
# except:
#     from urllib2 import Request, urlopen  # Python 2

# fields = {
# 'name' : 'sean',
# 'password' : 'password!',
# 'login' : 'LogIn'
# }
# opener = urllib.build_opener(
#     urllib.HTTPCookieProcessor()
# )
# request = urllib.Request(
#     "http://example.com/login",
#     urllib.urlencode(fields))

# url = opener.open(request)
# response = url.read()

# url = opener.open("http://example.com/dashboard")
# response = url.read()

import requests

headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

fields = {
'name' : 'sean',
'password' : 'password!',
'login' : 'LogIn'
}

r = requests.get('http://example.com', headers=headers, cookies=fields)
print(r.text)
