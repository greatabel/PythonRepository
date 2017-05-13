import requests

url = 'http://httpbin.org/post'

parms = {
   'name1' : 'value1',
   'name2' : 'value2'
}

headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}

resp = requests.post(url, data=parms, headers=headers)

# Decoded text returned by the request
text = resp.text

from pprint import pprint
pprint(resp.json)