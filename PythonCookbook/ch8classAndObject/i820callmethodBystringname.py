import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x,self.y)

    def distance(self,x,y):
        return math.hypot(self.x - x, self.y - y)
if __name__ == '__main__':
    p = Point(3, 4)
    d = getattr(p,'distance')(0,0)
    print('d=',d)

    import operator
    caller = operator.methodcaller('distance',0,0)(p)
    print('d2=',caller)

    points = [
    Point(1, 2),
    Point(3, 0),
    Point(10, -3),
    Point(-5, -7),
    Point(-1, 8),
    Point(3, 2)
    ]

    # Sort by distance from origin (0, 0)
    points.sort(key=operator.methodcaller('distance', 0, 0))
    for p in points:
        print(p)
