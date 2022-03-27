# coding=utf-8
# https://www.jianshu.com/p/ab7d1ebba3bf
# mac默认/usr/bin/python 是 python2.7，最好不要改变
# 另外注意服务是： 没有输入，具体看图：https://www.jianshu.com/p/0e9e5c2cb2a2

# 使用捷径app

import sys
import re

content = ''


for i in range(6):
    t = sys.stdin.readline()
    content += t
    if '摘录来自' in content:
    # if len(content) > 350:
        break

content = content.replace("摘录来自","").strip()
if '“' in content:
    s = content.index('“')
    if s != None:
        content = content[s+1:]
if content is not None:
    if content[-1] == '”':
        content = content[:-1]

print(content)