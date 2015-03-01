print ' range(10)=',range(10)
print "--"*5
print 'range(5)=',range(5)
print 'range(5,10)=',range(5,10)
print 'range(10,20)',range(10,20)

a = ['Mary', 'had', 'a', 'little', 'lamb']
print a

index = 0
for i in a :
 print index,'=',i
 index=index+1



print len(a)
print range(len(a))

for i in range(len(a)):
  print i, a[i]


print '-'*20,'randrange','-'*20

from random import randrange, choice
import random
from time import ctime

print "randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2)
print "randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2)
for i in range(10):
 print "randrange(80, 100, 2) : ", random.randrange(80, 100)
 print 'ctime(random.randrange(2**30, 2**32))=',ctime(random.randrange(2**29, 2**30))

import re
pattern='^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
for i in range(10):
 data=ctime(random.randrange(2**29, 2**30))
 print data
 m=re.match(pattern,data)
 print 'm.group()=',m.group()
 

from string import ascii_lowercase as lc
print 'lc=',lc
print 'lc=',lc
for i in range(25): 
 print choice(range(25))
 print 'choice(lc)=',choice(lc)

print ''.join(choice(lc) for j in range(115))
 







