import math
s1 = float(input("s1:"))
s2 = float(input("s2:"))
s3 = float(input("s3:"))
s = ( s1 + s2 + s3 )/2
area = math.sqrt(s * (s -s1) * (s - s2) * (s - s3))
print("erea is :%.02f" %area)