#http://blog.csdn.net/gzlaiyonghao/article/details/1656969
class Fruit(object):
       pass
class GiftMixin(object):
       def is_gift_fruit(self):
              return True
class NotGiftMixin(object):
       def is_gift_fruit(self):
              return False
class PareMixin(object):
       def eat_method(self):
              return 'Pare'
class HuskMixin(object):
       def eat_method(self):
              return 'Husk'

class NativeMixin(object):
       def Locality(self):
              return 'Native'
class ForeignMixin(object):
       def Locality(self):
              return 'Foreign'
class Apple(ForeignMixin, GiftMixin, PareMixin, Fruit):pass #进口红富士
class Orange(NativeMixin, GiftMixin, HuskMixin, Fruit):pass
class Pear(NativeMixin, NotGiftMixin, PareMixin, Fruit):pass
class Banana(NativeMixin, NotGiftMixin, HuskMixin, Fruit):pass

if __name__ == '__main__':
    apple = Apple()
    orange = Orange()
    print(apple.is_gift_fruit(),apple.Locality(), orange.is_gift_fruit(), orange.Locality())
