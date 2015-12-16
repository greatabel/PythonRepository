from linearbag import Bag

myBag = Bag()
myBag.add(100)
myBag.add(101)
myBag.add(102)
myBag.add(103)

value = int(input("Guess a value contained in the bag."))
if value in myBag:
    print("contain it!", value)
else:
    print("The bag does not contain the value", value)

