# lambda替代单行函数
def funs(x):
    return (x*2)

f = lambda x: x*2

print(funs(2))
print(f(2))

def add(x, y):
    return x + y

add_lambda = lambda x,y: x + y
most_args = lambda *z: z

print(add(2,4))
print(add_lambda(2,4))
print(most_args(1,2,"most"))

#内建函数filter(),map(),reduce()
from random import randint as ri

allNums = []

for eachNum in range(9):
    allNums.append(ri(1,99))

print("allNums",allNums)

for item in filter(lambda n: n%2, allNums):
    print(item)

for i in map(lambda x, y: x + y, [1,3,5], [2,4,6]):
    print('#',i)
for j in map(lambda x, y: (x,y), [1,3,5], [2,4,6]):
    print(j)

import functools
for i in range(5):
    print("i=",i)
print('the total is:', functools.reduce((lambda x,y: x+y), range(5)))
