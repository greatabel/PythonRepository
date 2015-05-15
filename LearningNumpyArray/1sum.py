import numpy as np

import sys
from datetime import datetime

#http://stackoverflow.com/questions/9091044/python-3-2-strange-error-with-range-type-in-list
def pythonsum(n):
   a = list(range(n))
   b = list(range(n))
   c = []

   for i in range(len(a)):
       a[i] = i ** 2
       b[i] = i ** 3
       c.append(a[i] + b[i])

   return c

def numpysum(n):
	a = np.arange(n) ** 2
	b = np.arange(n) ** 3
	c = a + b
	return c


size = int(sys.argv[1])

start = datetime.now()
c = pythonsum(size)
delta = datetime.now() - start
print(c)
print("pythonsum microsends %d"  %(delta.microseconds))

start = datetime.now()
c = numpysum(size)
delta = datetime.now() - start
print(c)
print("numpysum microsends %d"  %(delta.microseconds))
