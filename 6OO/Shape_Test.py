import Shape

a = Shape.Point()
print("repr(a)=",repr(a))
b = Shape.Point(3,4)
print(str(b))
print("b.distance_from_origin()=",b.distance_from_origin())
b.x = -19
print(str(b))
print( a==b, a!=b)