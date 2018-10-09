import requests
from os import environ
import json
import simplejson


qy_wechat_corpid = environ.get('qy_wechat_corpid')
qy_wechat_corpsecret = environ.get('qy_wechat_corpsecret')
qy_wechat_agentid = environ.get('qy_wechat_agentid')
qy_wechat_touser = environ.get('qy_wechat_touser')



url_get_token = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'\
                    .format(qy_wechat_corpid, qy_wechat_corpsecret)
r = requests.get(url_get_token)
d = json.loads(r.text)
print('d=', d)



url_get_send = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}'\
                    .format(d['access_token'])

send_msg_json = {
   "touser" : qy_wechat_touser,

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




class Fetcher:
    TOKEN_URL = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s'
    SEND_MSG_URL = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s'
    def get_access_token():
        r = requests.get(TOKEN_URL % (qy_wechat_corpid, qy_wechat_corpsecret))
        d = json.loads(r.text)



