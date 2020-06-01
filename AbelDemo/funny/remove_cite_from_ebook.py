import sys
import re
test = '''
“当我问她如何冒着重大风险行动时，她说：“每当我考虑到风险时，我会开始想象，冒险行动之后可能会出现的最佳结果。我会想象，要是冒险成功，一切都能成为现实。然后，我会想象冒险行动之后可能会出现的最糟情况。我会问自己能否处理最糟的情况，每次我都知道我能处理。也许我移居加拿大之后，事情并不如意。我最后可能会身无分文、孑然一身，但我知道我永远可以选择回家。但之后，我想象了可能出现的最佳结果，我会开始一段新生活，在这个新的国度交很多朋友、找到爱情、生儿育女。然后，我把这幅画面固定在我眼前。每当我的信心开始动摇时，我都会想象自己正为之奋斗的最佳结果。我会一直提醒自己，比失败的后果更糟的是离开了可能会出现的好结果。”

摘录来自: 约翰·B.伊佐. “人生没有后悔药。” Apple Books. 
'''


import sys
import re
content = ''
#从stdin里读取内容
for t in sys.stdin:
   content += t

# content = test

#利用正则表达式来查找原文并去除添加的引用信息
p = re.compile('“(.+)”\n\n摘录来自:')

search_c = p.search(content)
if search_c is not None:

    copy = search_c.group(1)

    #用print函数把结果传回Automator
    if copy:
        if copy.count('“')!= copy.count('”'):
            copy += '”'
        print(copy)