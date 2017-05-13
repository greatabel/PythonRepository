class Parent(object):
 
  def implicit(self):
    print "parent implicit()"

class Child(Parent):
  pass

dad=Parent()
son=Child()

dad.implicit()
son.implicit()



