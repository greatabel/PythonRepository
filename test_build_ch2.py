# -*- coding: utf-8 -*-
print('测试中文')
test = '1234'
print(test)
# import pdb 

for i in range(10,20):
	print('i='+str(i))

# pdb.set_trace()
test += '567'
print('test build1'+test)
print('end')

import xml.sax.saxutils
t = xml.sax.saxutils.escape("http://www.example.com/view?widget=3&count>2")
print( t )


import asyncio

def hello_world(loop):
    print('Hello World')
    loop.stop()

loop = asyncio.get_event_loop()

# Schedule a call to hello_world()
loop.call_soon(hello_world, loop)

# Blocking call interrupted by loop.stop()
loop.run_forever()
loop.close()

import sys, pdb
sys.excepthook = lambda x,y,z: pdb.pm()


