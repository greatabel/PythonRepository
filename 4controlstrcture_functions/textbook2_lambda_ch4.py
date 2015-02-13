s = lambda x: "" if x == 1 else "s"
#唯一时候添加s，不为1不添加
count = 10
print("{0} file{1} processed".format(count,s(count)))
count = 1
print("{0} file{1} processed".format(count,s(count)))

#（group,number,name)
elements =[(2,12,"Mg"),(1,12,"Na"),(1,3,"Li"),(2,4,"Be")]
elementsA = elements.copy()
elementsB = elements.copy()
print(elements)
elements.sort()
print("After sort:")
print(elements)

print("elementsA=", elementsA)
print("use number name to sort ,ignore group:")
elementsA.sort(key=lambda e:(e[1],e[2]))
print(elementsA)

#根据大小写不敏感的name和number
print("elementsB=", elementsB)
elementsB.sort(key=lambda e:(e[2].lower(),e[1]))
print(elementsB)

area = lambda b,h:0.5 * b * h
def areaA(b,h):
	return 0.5 * b * h
print("area=", area(20,10))
print("areaA=", areaA(10, 20))

# another Scenario to use lambda is dict
import collections
minus_one_dict = collections.defaultdict(lambda:-1)
# test by not assign value->
print("minus_one_dict=", minus_one_dict[0])

point_zero_dict = collections.defaultdict(lambda:(0,0))
print("point_zero_dict=", point_zero_dict[1])

message_dict = collections.defaultdict(lambda: "No message available")
print("message_dict=", message_dict[2])

def product_pessimistic(*args):
	assert all(args),"0 argument here"
	result = 1
	for arg in args:
		result *= arg
	return result

# product_pessimistic(1,2,3,0)

def product_optimistic(*args):
	
	result = 1
	for arg in args:
		result *= arg
	assert result,"0 argument"
	return result

# product_optimistic(1,2,3,0)

number = input('Enter a positive number:')
print(number)
assert (int(number) > 0), 'Only positive numbers are allowed!'

