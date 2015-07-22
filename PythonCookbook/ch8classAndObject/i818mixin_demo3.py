#  http://guangboo.org/2013/01/28/python-mixin-programming
class A:
  def get_a(self):
    print('A')




if __name__ == '__main__':
    apple = Apple()
    orange = Orange()
    print(apple.is_gift_fruit(),apple.Locality(), orange.is_gift_fruit(), orange.Locality())
