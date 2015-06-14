#http://stackoverflow.com/questions/3182183/creating-a-list-of-objects-in-python
import sys

class MyClass(object):
    def __init__(self,number=None,name=None,description=None):
        self.number = number
        self.name = name
        self.description = description


def Create():
	my_objects = []	
	my_objects.append(MyClass(1,"H","HHHH1"))
	my_objects.append(MyClass(2,"He","HHHH2"))
	my_objects.append(MyClass(3,"Li","HHHH3"))

	for obj in my_objects :
	    print(obj.name,obj.description)
	return my_objects





def main():
	olist =Create()
	myinput = input("Enter:")
	try:
		
		for item in olist:
			try:
				intinput = int(myinput)
				if item.number == intinput:
					print("value=",item.description)
			except:
				if item.name == str(myinput):
					print("value 2 = ",item.description)

	except:
		quit()


	

	

        
if __name__ == "__main__":
    main()
