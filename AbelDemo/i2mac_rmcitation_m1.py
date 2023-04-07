# coding=utf-8
# https://www.jianshu.com/p/ab7d1ebba3bf
# mac默认/usr/bin/python 是 python2.7，最好不要改变
# 另外注意服务是： 没有输入，具体看图：https://www.jianshu.com/p/0e9e5c2cb2a2

# 使用捷径app

# import sys
# import re

# content = ''


# for i in range(6):
#     t = sys.stdin.readline()
#     content += t
#     if '摘录来自' in content:
#     # if len(content) > 350:
#         break

# content = content.replace("摘录来自","").strip()
# # 处理英文时候有问题
# # content = content.replace(" ","")
# if '“' in content:
#     s = content.index('“')
#     if s != None:
#         content = content[s+1:]
# if content is not None:
#     if content[-1] == '”':
#         content = content[:-1]

# print(content)
import sys
import re

content = ''

for i in range(6):
    t = sys.stdin.readline()
    content += t
    if '摘录来自' in content:
        break

content = content.replace("摘录来自", "").strip()

# 判断前引号和后引号的数量
num_start_quotes = content.count('“')
num_end_quotes = content.count('”')

# 如果前引号数量大于后引号数量，说明需要删除最后一个前引号
if num_start_quotes > num_end_quotes:
    # 查找最后一个前引号的位置
    last_start_quote_index = content.rfind('“')
    if last_start_quote_index != -1:
        content = content[:last_start_quote_index] + content[last_start_quote_index + 1:]

print(content)

