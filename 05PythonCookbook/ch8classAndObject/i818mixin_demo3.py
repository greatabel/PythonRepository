#  http://guangboo.org/2013/01/28/python-mixin-programming
class A:
    def get_a(self):
        print('A')

class B:
    def get_b(self):
        print('B')

class C(A,B):
    pass
  


if __name__ == '__main__':
    c = C()
    c.get_a()
    c.get_b()
