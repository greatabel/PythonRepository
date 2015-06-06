G = 9.8
iV = float(input("input initial speed(m/s):"))
height = float(input(" height to drop(m):"))

import math
v = math.sqrt( iV **2 + 2*G*height )
print("fall speed: %.02f m/s" %(v))