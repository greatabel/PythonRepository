# coding=utf-8
# https://www.jianshu.com/p/ab7d1ebba3bf
# mac默认/usr/bin/python 是 python2.7，最好不要改变
# 另外注意服务是： 没有输入，具体看图：https://www.jianshu.com/p/0e9e5c2cb2a2

from __future__ import print_function
import sys
import sys
import re
content = ''
#从stdin里读取内容
# for t in sys.stdin:
# 	content += t
# #利用正则表达式来查找原文并去除添加的引用信息
# p = re.compile('“(.+)”\n\n摘录来自:')
# if content is not None:
# 	if p.search(content) is not None:
# 		copy = p.search(content).group(1)
# 		#用print函数把结果传回Automator
# 		if copy:
# 			print(copy)
# 	else:
# 		print("")
# else:
# 	print("")

# sys.stdin = open('simulatedInput.txt','r') 

while True:
    t = sys.stdin.readline()
    content += t
    if '摘录来自' in content:
    	break
# for t in sys.stdin.readline():

# 	content += t
# print('#'*20,content)

#利用正则表达式来查找原文并去除添加的引用信息
p = re.compile('“(.+)”\n\n摘录来自:')
if content is not None:
	if p.search(content) is not None:
		copy = p.search(content).group(1)
		#用print函数把结果传回Automator
		if copy:
			print(copy)
	else:
		print("")
else:
	print("")