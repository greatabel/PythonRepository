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

# print('d=', d)

ACCESS_TOKEN = d['access_token']
print(ACCESS_TOKEN)


# https://segmentfault.com/q/1010000002663185
headers = {'Content-Type': 'application/json', "charset": "utf-8"}

url_grouplist = 'https://api.weixin.qq.com/cgi-bin/groups/get?access_token=' + ACCESS_TOKEN
# group_json = {
#                   "begin": 0,
#                   "count": 10
#              }
# json_string = simplejson.dumps(group_json, ensure_ascii=False).encode('utf8')
r_group = requests.get(url_grouplist,  headers=headers)
dev_group_id = -1
groups = json.loads(r_group.text)['groups']
for item in groups:
    if item['name'] == 'dev':
        dev_group_id = item['id']
print('dev_group_id=', dev_group_id)



menu_json = {
    "button": [
        {
            "type": "view",
            "name": "MeoMo测量",
            "url": "https://app.meomo.cn"
        },
        {
            "name": "客户服务", 
            "sub_button": [
                {
                    "type": "media_id", 
                    "name": "售后服务", 
                    "media_id": "get from i1material.py result"

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
        }
    ]
}

conditional_menu_json = {
    "button": [
        {
            "type": "view",
            "name": "MeoMo测量",
            "url": "https://app.meomo.cn"
        },
        {
            "name": "客户服务", 
            "sub_button": [
                {
                    "type": "media_id", 
                    "name": "售后服务", 
                    "media_id": "get from i1material.py result"

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
                    "url": "https://app-test.meomo.cn"

                 }, 
                {
                    "type": "view", 
                    "name": "Dev", 
                    "url": "https://app-dev.meomo.cn"

                 }, 
                {
                    "type": "view", 
                    "name": "Exp", 
                    "url": "https://app-exp.meomo.cn"

                 }, 
                {
                    "type": "view", 
                    "name": "Local", 
                    "url": "http://app-local.meomo.cn/"

                 }, 
            ]
        }
    ],
    "matchrule":{ "tag_id": dev_group_id}
}

url_menu = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=' + ACCESS_TOKEN
url_condition_menu = 'https://api.weixin.qq.com/cgi-bin/menu/addconditional?access_token=' + ACCESS_TOKEN

json_string = simplejson.dumps(menu_json, ensure_ascii=False).encode('utf8')
condition_json_string = simplejson.dumps(conditional_menu_json, ensure_ascii=False).encode('utf8')
# print(condition_json_string)
#  设置menu
r1 = requests.post(url_menu, data=json_string, headers=headers)
print('r1.text = ', r1.text)
r2 = requests.post(url_condition_menu, data=condition_json_string, headers=headers)
print('r2.text = ', r2.text)