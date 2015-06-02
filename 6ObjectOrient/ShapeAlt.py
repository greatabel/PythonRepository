# coding:utf-8
import math

class Point:

    def __init__(self, x=0, y=0):
    	#http://stackoverflow.com/questions/15549429/doctest-dictionary-equality 添加了 __repr__ 后可以才可以通过的原因在问题的评论
        """A 2D cartesian coordinate

        >>> point = Point()
        >>> point
        Point(0, 0)
        """
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __repr__(self):
        return ("{0.__class__.__name__}({0.x!r}, {0.y!r})".format(
                self))


    # def __str__(self):
    #     return "({0.x!r}, {0.y!r})".format(self)

if __name__ == "__main__":
	import doctest
	doctest.testmod()