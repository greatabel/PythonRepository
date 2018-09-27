import requests
from os import environ
import json
import simplejson


qy_wechat_corpid = environ.get('qy_wechat_corpid')
qy_wechat_corpsecret = environ.get('qy_wechat_corpsecret')
print(qy_wechat_corpid, qy_wechat_corpsecret)
url_get_token = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'\
                    .format(qy_wechat_corpid, qy_wechat_corpsecret)
r = requests.get(url_get_token)
d = json.loads(r.text)
print('d=', d)