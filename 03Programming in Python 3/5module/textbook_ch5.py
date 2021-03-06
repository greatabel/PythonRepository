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
path = os.getcwd()
print(path)
mytar = tarfile.open("sample.tar")
# mytar.extractall()
mytar.extractall(path=os.getcwd()+"/abeltest")
mytar.close()

#os模块--------------------------------
date_from_name = {}
for name in os.listdir(path):
	fullname = os.path.join(path, name)
	if os.path.isfile(fullname):
		date_from_name[fullname] = os.path.getmtime(fullname)

print(date_from_name)

#io模块--------------------------------
print("io------->")
import io
output = io.StringIO()
output.write('First line.\n')
print('Second line.', file=output)

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'
contents = output.getvalue()
print("contents="+contents)
# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
output.close()

#optparse模块--------------------------------
print("optparse--->")
import optparse
parser = optparse.OptionParser()
parser.add_option("-w","--maxwidth", dest="maxwidth",type="int",
	help=("the maximum number of characters that can be "
		"output to string fields [default: %default]"))
parser.add_option("-f","--format",dest ="format",
	help=("the format used for oputtting numbers"
		"[default: %default]"))
parser.set_defaults(maxwidth=100, format=".0f")
opts, args = parser.parse_args()
print(opts, args)



#calendar,datetime,time模块--------------------------------
import calendar, datetime,time
moon_datetime_a = datetime.datetime(2015, 2, 19,13,1,30)
moon_time = calendar.timegm(moon_datetime_a.utctimetuple())

print("moon_datetime_a=", moon_datetime_a)
print("moon_time=", moon_time)

moon_datetime_b = datetime.datetime.utcfromtimestamp(moon_time)
print(moon_datetime_a.isoformat())
print(moon_datetime_b.isoformat())
print(time.strftime("%Y-%m-%T%H:%M:%S",time.gmtime(moon_time)))

#排序模块bisect https://docs.python.org/2/library/bisect.html--------------------------------
import bisect
print("bisect=",dir(bisect))
data = [4,2,9,12,1]
print(data)
data.sort()
print(data)
bisect.insort(data, 5)
print(data)
print('bisect.bisect(data,10)=',bisect.bisect(data,10))
print(bisect.bisect(data,1))
print(bisect.bisect(data,12))

#UserList,  UserDict,weakref弱引用 模块--------------------------------
print("#从py3 开始 UserList模块被移到---->> collections")
from collections import UserList
class AutoList(UserList):
	def __setitem__(self,i,item):
		if i == len(self.data):
			self.data.append(item)
		else:
			self.data[i] = item
list = AutoList()
for i in range(10):
	list[i] = 2 * i
print(list)

from collections import UserDict
class FileInfo(UserDict):
	"store file metadata"
	def __init__(self,filename =None):
		UserDict.__init__(self)
		self["name"] = filename

FileDic = FileInfo()
for i in range(100,110):
	FileDic[i-100]="file"+str(i)
print(FileDic)
#----------------------------

import weakref
print("weakref=",dir(weakref))
class TestObj:
    pass
a = TestObj()
#建立一个a的弱引用
x = weakref.ref(a)
print( x)
print( x())

#引用对象销毁时的回调函数-----------------
class  TestObjA:
	pass

def test_func(reference):
	print("hello from callback function")
	print(reference,'this weak reference is no longer valid')

tA = TestObjA()
x = weakref.ref(tA,test_func)
del tA
#使用代理和使用普通weakref的区别就是不需要()，可以像原对象一样地使用proxy访问原对象的属性
class TestObjB:
    def __init__(self):
        self.test_attr = 100
def test_funcB(reference):
    print('Hello[B] from Callback function!')
   
a = TestObjB()
print('a here=', dir(a))
#建立一个对a的代理(弱引用)
x = weakref.proxy(a, test_funcB)
print(a.test_attr)
print( x.test_attr)
del a

#-heapq模块---------------------------
import heapq
heapa = []
heapq.heappush(heapa,(5,"rest"))
heapq.heappush(heapa,(2,"work"))
heapq.heappush(heapa,(1,"study"))
heapq.heappush(heapa,(10,"haha"))
print("heapqa=",heapa)
for x in heapq.merge([1,3,5,8],[2,4,7],[0,1]):
	print(x,end=" ")
