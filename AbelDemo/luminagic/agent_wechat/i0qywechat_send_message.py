import requests
from os import environ
import json
import simplejson


qy_wechat_corpid = environ.get('QY_WECHAT_CORPID')
qy_wechat_corpsecret = environ.get('QY_WECHAT_CORPSECRET')
qy_wechat_agentid = environ.get('QY_WECHAT_AGENTID')

print(qy_wechat_corpid, qy_wechat_corpsecret, qy_wechat_agentid)
url_get_token = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'\
                    .format(qy_wechat_corpid, qy_wechat_corpsecret)
r = requests.get(url_get_token)
d = json.loads(r.text)
print('d=', d)

# app_get_token = 'https://qyapi.weixin.qq.com/cgi-bin/agent/get?access_token={}&agentid={}'\
#                     .format(d['access_token'], qy_wechat_agentid)
# r = requests.get(app_get_token)
# d = json.loads(r.text)
# print('d1=', d)

url_get_send = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}'\
                    .format(d['access_token'])

send_msg_json = {
   "touser" : "qy014eae0e386abc002844b25aa6|qy01fdaec53875bc00287cbdfd48|qy01b6ae873858bc0028f6c307ca",

   "msgtype" : "text",
   "agentid" : qy_wechat_agentid,
   "text" : {
       "content" : "你有新的客服通知，请登陆客服小程序查看"
   },
   "safe":0
}
json_string = simplejson.dumps(send_msg_json, ensure_ascii=False).encode('utf8')
headers = {'Content-Type': 'application/json', "charset": "utf-8"}

r1 = requests.post(url_get_send, data=json_string, headers=headers)
print('r1.text = ', r1.text)