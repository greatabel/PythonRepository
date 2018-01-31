#coding = utf-8
# https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1444738729

import requests
from os import environ
import json
import simplejson
import subprocess

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

url_getlist = "https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token=" + ACCESS_TOKEN

url_meterial = "https://api.weixin.qq.com/cgi-bin/material/add_news?access_token=" + ACCESS_TOKEN
# https://segmentfault.com/q/1010000002663185
headers = {"Content-Type": "application/json", "charset": "utf-8"}

content = "您好！感谢你购买并使用MeoMo产品.如果你对如何使用Meomo有疑惑，可以参考在线教学视频和在线指南。\
            其他问题，你可以浏览我们的FAQ，或许可以找到答案。 如果你仍然有问题，请直接在公众号留言联系\
            我们。我们的客服时间是周一到周五 早10:00-下午5:00"

get_json =  {
    "type":"image",
    "offset":0,
    "count":20
}
# Sp7vV5TVqSw7PQKK2VowS_DKIG10RbWp1KIVflXAAmA
meterial_json = {
    "articles": [
        {
            "title": "售后服务",
            "thumb_media_id": "Sp7vV5TVqSw7PQKK2VowS_DKIG10RbWp1KIVflXAAmA",
            "author": "Luminagic",
            "show_cover_pic": 0,
            "content": content,
            "content_source_url": "http://www.meomo.cn/#faq"
        },

    ],
}

json_string = simplejson.dumps(meterial_json, ensure_ascii=False).encode('utf8')
get_json_string = simplejson.dumps(get_json, ensure_ascii=False).encode('utf8')

r0 = requests.post(url_getlist, data=get_json_string, headers=headers)
print('get list :r0.text = ', r0.text)
media_id = -1
groups = json.loads(r0.text)['item']
for item in groups:
    if item['name'] == 'service_test.jpg':
        media_id = item['media_id']


meterial_json = {
    "articles": [
        {
            "title": "售后服务",
            "thumb_media_id": media_id,
            "author": "Luminagic",
            "show_cover_pic": 0,
            "content": content,
            "content_source_url": "http://www.meomo.cn/#faq"
        },

    ],
}

r1 = requests.post(url_meterial, data=json_string, headers=headers)
print('r1.text = ', r1.text)

# 上传照片
# bashCommand = "curl -F media=@service_test.jpg \"https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=" \
#                 + ACCESS_TOKEN +"\""
# output = subprocess.check_output(['bash','-c', bashCommand])
# print('output=', output)