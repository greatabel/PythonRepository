#coding = utf-8

import requests
from os import environ
import json
import simplejson

appids = environ.get('WECHAT_APPID')
if appids:
    appids = appids.split(',')
appsecrets = environ.get('CUSTOMCONNSTR_WECHAT_APPSECRET')
if appsecrets:
    appsecrets = appsecrets.split(',')

print(appids[0], appsecrets[0])
# 这里需要设置白名单 去公众平台后台
url_get_token = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'\
                    .format(appids[0], appsecrets[0])
r = requests.get(url_get_token)
d = json.loads(r.text)



ACCESS_TOKEN = d['access_token']
print(ACCESS_TOKEN)

menu_json = {
    "button": [
        {
            "type": "view",
            "name": "MeoMo测量",
            "url": "http://app.meomo.cn"
        },
        {
            "name": "客户服务", 
            "sub_button": [
                {
                    "type": "view", 
                    "name": "售后服务", 
                    "url": "http://www.meomo.cn/#faq"

                 }, 
                {
                    "type": "view", 
                    "name": "APP下载", 
                    "url": "http://www.meomo.cn/#app"

                 }, 
                {
                    "type": "view", 
                    "name": "在线专家咨询", 
                    "url": "http://www.meomo.cn/#_8"

                 }, 
            ]
        }, 
        {
            "name": "开发", 
            "sub_button": [
                {
                    "type": "view", 
                    "name": "Test", 
                    "url": "http://app-test.meomo.cn/"

                 }, 
                {
                    "type": "view", 
                    "name": "Dev", 
                    "url": "http://app-dev.meomo.cn/"

                 }, 
                {
                    "type": "view", 
                    "name": "Exp", 
                    "url": "http://app-exp.meomo.cn/"

                 }, 
                {
                    "type": "view", 
                    "name": "Local", 
                    "url": "http://app-local.meomo.cn/"

                 }, 
            ]
        }
    ]
}
# https://segmentfault.com/q/1010000002663185
headers = {'Content-Type': 'application/json', "charset": "utf-8"}
url_menu = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=' + ACCESS_TOKEN
json_string = simplejson.dumps(menu_json, ensure_ascii=False).encode('utf8')
r1 = requests.post(url_menu, data=json_string, headers=headers)
print('r1.text = ', r1.text)