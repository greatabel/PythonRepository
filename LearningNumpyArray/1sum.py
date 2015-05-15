import numpy as np

import sys
from datetime import datetime

def pythonsum(n):
   a = list(range(n))
   b = list(range(n))
   c = []

   for i in range(len(a)):
       a[i] = i ** 2
       b[i] = i ** 3
       c.append(a[i] + b[i])

   return c

print(pythonsum(3))
