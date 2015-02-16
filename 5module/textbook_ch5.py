# -*- coding: utf-8 -*-
import heapq

heap = []
heapq.heappush(heap, "2rest")
heapq.heappush(heap, "1work")
heapq.heappush(heap, "3study")

print(heap)

#base64例子,中文UTF-8编码base64报错http://ipfans.github.io/2014/03/python-base64-encode-utf-8error.html
import base64
_str = u"你好世界"    
encoded = base64.b64encode(_str.encode('utf-8'))
print(encoded)
print(base64.b64decode(encoded).decode('utf-8'))

_str=u'i\xb7\x1d\xfb\xef\xff'
print(base64.b64encode(_str.encode('utf-8')))
print(base64.urlsafe_b64encode(_str.encode('utf-8')))

#解压缩的例子 －－－－－－－－－－－－－
import tarfile
print("压缩->")
tar = tarfile.open("sample.tar","w")
for name in ["test_ch5.txt","test1_ch5.txt"]:
	tar.add(name)
tar.close()

print("解压－>")
import os
print(os.getcwd())
mytar = tarfile.open("sample.tar")
# mytar.extractall()
mytar.extractall(path=os.getcwd()+"/abeltest")
mytar.close()