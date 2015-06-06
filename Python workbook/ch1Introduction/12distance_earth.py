t1 = float(input("latitude? "))
g1 = float(input("longitude? "))
t2 = float(input("2rd latitude? "))
g2 = float(input("2rd longitude? "))
import math

t1 = math.radians(t1)
t2 = math.radians(t2)
g1 = math.radians(g1)
g2 = math.radians(g2)

distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1-g2))
# 22.54587746 , 114.12873077
print("distance: %.02f" % distance)
