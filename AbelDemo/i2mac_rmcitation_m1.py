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
        break

# 删除"摘录来自"之后的所有文本
content = content[:content.index("摘录来自")].strip()

# 删除类似 [48] 这种引用格式的内容
content = re.sub(r'\[\d+\]', '', content).strip()

# 处理首位前引号和其对应的后引号
if content.startswith("“") and content.endswith("”"):
    content = content[1:-1]
elif content.startswith("“") and content.count("“") < content.count("”"):
    content = content[1:]
    last_quote_index = content.rindex("”")
    content = content[:last_quote_index] + content[last_quote_index+1:]

print(content)

