import math
import doctest

"""
运行python Shape.py 
如果doctest通过，不会有任何输出。可以加-v参数来查看测试细节
"""
class Point:
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y

	def distance_from_origin(self):
		return math.hypot(self.x,self.y)

	def __eq__(self,other):
		return self.x == other.x and self.y == other.y

	def __repr__(self):
		return "Point({0.x!r},{0.y!r})".format(self)

	def __str__(self):
		return "({0.x!r},{0.y!r})".format(self)


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        """A Circle
        >>> circle = Circle(2)
        >>> circle
        Circle(2, 0, 0)
        """
        super().__init__(x, y)
        self.radius = radius

         
    def edge_distance_from_origin(self):
        """The distance of the circle's edge from the origin
        >>> circle = Circle(2, 3, 4)
        >>> circle.edge_distance_from_origin()
        3.0
        """
        return abs(self.distance_from_origin() - self.radius)


    def area(self):
        """The circle's area
        >>> circle = Circle(10)
        >>> a = circle.area()
        >>> int(a)
        314
        """
        return math.pi * (self.radius ** 2)


    def circumference(self):
        """The circle's circumference
        >>> circle = Circle(3)
        >>> d = circle.circumference()
        >>> int(d)
        18
        """
        return 2 * math.pi * self.radius


    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)


    def __repr__(self):
        return "Circle({0.radius!r}, {0.x!r}, {0.y!r})".format(self)


    def __str__(self):
        return repr(self)

if __name__ == "__main__":
    doctest.testmod()
