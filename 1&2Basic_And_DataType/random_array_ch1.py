print("Hello","World!")

x = "blue"
y = "green"
z = x
print(x,y,z)

route = 866
print(route,type(route))
route = "North"
print(route,type(route))

print( len(("one",)) )
print( len([1,2,3,"pause",5]))
print(len("great"))

x=["test",1,-11,"desk",12]
print(x)
x.append("more")
print(x)

##############
def get_int(msg,minimum,default):
	while True:
		try:
			line = input(msg)
			if not line and  default is not None:
				return default
			i = int(line)
			if i < minimum:
				print("must be >=", minimum)
			else:
				return i
		except ValueError as err:
			print(err)


############### get value ######
rows = get_int("rows:",1,None)
columns = get_int("columns:",1,None)
minimum = get_int("minimum(or Enter for 0):",-1000000,0)

default = 1000
if default < minimum:
	default = 2 * minimum
maximum = get_int("maximum (or Enter for" + str(default)+"):",
			minimum,default)


############### show value ######
import random

row = 0
while row < rows:
	line = ""
	column = 0
	# print('columns=',columns)
	while column < columns:
		i = random.randint(minimum,maximum)
		# print('i=',i)
		s = str(i)
		# print('len(s)=',len(s))
		while len(s) < 10:
			s = " " + s
		line += s
		column += 1
	print(line)
	row += 1

