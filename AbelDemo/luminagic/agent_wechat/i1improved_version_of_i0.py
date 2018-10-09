import requests
from os import environ
import json
import simplejson


qy_wechat_corpid = environ.get('qy_wechat_corpid')
qy_wechat_corpsecret = environ.get('qy_wechat_corpsecret')
qy_wechat_agentid = environ.get('qy_wechat_agentid')
qy_wechat_touser = environ.get('qy_wechat_touser')




class MsgSender:
    TOKEN_URL = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s'
    SEND_MSG_URL = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s'



    def get_access_token(self):
        r = requests.get(self.TOKEN_URL % (qy_wechat_corpid, qy_wechat_corpsecret))
        resp = json.loads(r.text)
        if resp['errcode'] or resp['access_token'] == '':
            return None
        return resp['access_token']

    def post_wq_msg(self, access_token, qy_wechat_touser, qy_wechat_agentid):
        SEND_MSG_JSON = {
           "touser" : qy_wechat_touser,

           "msgtype" : "text",
           "agentid" : qy_wechat_agentid,
           "text" : {
               "content" : "你有新的客服通知，请登陆客服小程序查看."
           },
           "safe":0
        }
        json_string = simplejson.dumps(SEND_MSG_JSON, ensure_ascii=False).encode('utf8')
        headers = {'Content-Type': 'application/json', "charset": "utf-8"}
        r = requests.post(self.SEND_MSG_URL % (access_token), data=json_string, headers=headers)
        resp = json.loads(r.text)
        print('r1.text = ', resp)

    def send(self):
        access_token = self.get_access_token()
        print('access_token=', access_token)
        self.post_wq_msg(access_token, qy_wechat_touser, qy_wechat_agentid)



f = MsgSender().send()



