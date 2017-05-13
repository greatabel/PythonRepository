# usage:
# (env1)wanchangdeMacBook-Pro:ch15C_extension wanchang$ make
# gcc -shared -undefined dynamic_lookup sample.c -o libsample.so
# (env1)wanchangdeMacBook-Pro:ch15C_extension wanchang$ cd 1access_C_code_using_ctypes/
# (env1)wanchangdeMacBook-Pro:1access_C_code_using_ctypes wanchang$ ls
# __pycache__ i1example.py    sample.py
# (env1)wanchangdeMacBook-Pro:1access_C_code_using_ctypes wanchang$ python3 i1example.py 
# 7
# 1
# 0
# (5, 2)
# 2.0
# 4.242640687119285


import sample
print(sample.gcd(35,42))
print(sample.in_mandel(0,0,500))
print(sample.in_mandel(2.0,1.0,500))
print(sample.divide(42,8))
print(sample.avg([1,2,3]))
p1 = sample.Point(1,2)
p2 = sample.Point(4,5)
print(sample.distance(p1,p2))
