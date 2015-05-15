#non-literal object creation
y = '6'
x = int(y)
print(x)


z = float('6.3')
w = str(z)
u = list(w)
print(u)

#calling methods on Objects
x = 'how are you'
y = x.upper()
print(y)

myList = [1,2,3]
myList.reverse()
print(myList)


class Dog:
 # This is the constructor for the class. It is called whenever a Dog
 # object is created. The reference called "self" is created by Python
 # and made to point to the space for the newly created object. Python
 # does this automatically for us but we have to have "self" as the first
 # parameter to the __init__ method (i.e. the constructor).
def __init__(self, name, month, day, year, speakText):
	self.name = name
	self.month = month
	self.day = day

 # object. The current object appears on the left hand side of the dot (i.e.
 # the .) when the method is called.
 def speak(self):
 	return self.speakText

 # Here is an accessor method to get the name
 def getName(self):