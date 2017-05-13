from urllib import request, parse


url = 'https://api.douban.com/v2/book/search'

# Dictionary of query parameters (if any)
parms = {
   'count' : '3',
   'q' : 'hello'
}

# Encode the query string
querystring = parse.urlencode(parms)

# Make a GET request and read the response

u = request.urlopen(url+'?' + querystring)
resp = u.read()

import json
from pprint import pprint
print(resp.decode('utf-8'))
print('#'*10)
json_resp = json.loads(resp.decode('utf-8'))
pprint(json_resp)