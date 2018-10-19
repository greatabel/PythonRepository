import requests
from os import environ
import json




qy_wechat_corpid = environ.get('qy_wechat_corpid')
qy_wechat_corpsecret = environ.get('qy_wechat_corpsecret')
qy_wechat_agentid = environ.get('qy_wechat_agentid')
qy_wechat_touser = environ.get('qy_wechat_touser')


qy_cache = ''


TOKEN_URL = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s'
SEND_MSG_URL = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s'

def get_access_token():
    r = requests.get(TOKEN_URL % (qy_wechat_corpid,
                     qy_wechat_corpsecret))
    resp = json.loads(r.text)
    if resp['errcode'] or resp['access_token'] == '':
        return None
    # qy_cache.set('qy_msg_access_token', resp['access_token'], timeout=7200)
    return resp['access_token']

def post_wq_msg(access_token, qy_wechat_touser, qy_wechat_agentid):
    send_msg_json = {
       "touser": qy_wechat_touser,
       "msgtype": "text",
       "agentid": qy_wechat_agentid,
       "text": {
           "content": "你有新的客服通知，请登陆客服小程序查看."
       },
       "safe": 0
    }
    json_string = json.dumps(send_msg_json, ensure_ascii=False).encode('utf8')
    headers = {"Content-Type": "application/json", "charset": "utf-8"}
    r = requests.post(SEND_MSG_URL % (access_token), data=json_string, headers=headers)
    resp = json.loads(r.text)
    if resp['errcode'] == 40014 or resp['errmsg'] == 'invalid access_token':
        access_token = self.get_access_token()
        r = requests.post(SEND_MSG_URL % (access_token), data=json_string, headers=headers)
        resp = json.loads(r.text)
    return resp

def send():
    # access_token = qy_cache.get('qy_msg_access_token')
    # if access_token == '':
    access_token = get_access_token()
    r = post_wq_msg(access_token, qy_wechat_touser,
                         qy_wechat_agentid)
    return r



f = send()



