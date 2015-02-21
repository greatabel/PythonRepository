import Shape

a = Shape.Point()
print("repr(a)=",repr(a))
b = Shape.Point(3,4)
print(str(b))
print("b.distance_from_origin()=",b.distance_from_origin())
b.x = -19
print(str(b))
print( a==b, a!=b)

c = Shape.Circle(5,28,45)
print("c.distance_from_origin()=",c.distance_from_origin())