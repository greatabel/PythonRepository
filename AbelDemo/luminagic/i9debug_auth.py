import requests
from urllib.parse import urlencode
from os import environ

wechat_api_token = 'https://api.weixin.qq.com/sns/oauth2/access_token'
appid = environ['WECHAT_APPID']
appsecret = environ['CUSTOMCONNSTR_WECHAT_APPSECRET']
code = '假造code'

query = [
    ('appid', appid),
    ('secret', appsecret),
    ('code', code),
    ('grant_type', 'authorization_code'),
]

try:
    resp = requests.get(wechat_api_token, params=urlencode(query)).json()
    print('resp=', resp)
except requests.exceptions.HTTPError:
    abort(503, description='无法连接到微信')
if 'errcode' in resp:
    print('#'*10, 'in 403')
    abort(403, description='发生错误（' + resp['errmsg'] + '），请重试')