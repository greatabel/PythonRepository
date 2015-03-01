import os
import re

f=os.popen('who','r')
print 'f=',f
for eachLine in f:
 print re.split('\s\s+|\t',eachLine.rstrip())
f.close()

print '*'*20,'with','*'*20

with os.popen('who','r') as f:
    for eachLine in f:
      print(re.split('\s\s+|\t',eachLine.rstrip()))

from distutils.log import warn as printf

print '*'*20,'printf','*'*20
with os.popen('who', 'r') as f:
    for eachLine in f:
        printf(re.split('\s\s+|\t', eachLine.rstrip()))

with os.popen('who', 'r') as f:
 [printf(re.split('\s\s+|\t', eachLine.strip())) for eachLine in f]
