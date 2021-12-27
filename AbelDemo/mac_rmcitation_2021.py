# coding=utf-8
# https://www.jianshu.com/p/ab7d1ebba3bf
# mac默认/usr/bin/python 是 python2.7，最好不要改变
# 另外注意服务是： 没有输入，具体看图：https://www.jianshu.com/p/0e9e5c2cb2a2

from __future__ import print_function
import sys
import sys
import re
content = ''


# sys.stdin = open('simulatedInput.txt','r') 
# sys.stdin = open('simulatedInput_2021.txt','r') 

while True:
    t = sys.stdin.readline()
    content += t
    if '摘录来自' in content:
    	break
# for t in sys.stdin.readline():

def find_between(s, start, end):
	return (s.split(start))[1].split(end)[0]

r = find_between(content, "“", "”")
r = r.replace('[…]', '')
print(r)