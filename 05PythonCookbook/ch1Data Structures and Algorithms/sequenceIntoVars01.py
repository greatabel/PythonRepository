p = (4,5)
x,y = p
print(x,"and",y)

data = ['ACME',50,91.111,(2015,6,17)]
name,shares,price,date = data
print(name,shares,price,date )

#可分的不只是list，元祖 也可以是别的
s = 'Hello'
a,b,c,d,e = s
print(a,b,c,d,e)

#有时候不是需要所有的
data = ['ACME1',501,911.111,(2015,7,17)]
_,shares1,price1,_ = data
print(shares1,price1)
print("_其实是我们扔掉的变量，也是有内容")
print(_)
