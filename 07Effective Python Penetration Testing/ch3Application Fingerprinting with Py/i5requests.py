import requests

target_url = 'https://www.douban.com/'

response = requests.get(target_url)
# Response
print( response.status_code ) # Response Code
print( response.headers     ) # Response Headers
print( response.content     ) # Response Content
print( response.request.headers) # Headers we sent