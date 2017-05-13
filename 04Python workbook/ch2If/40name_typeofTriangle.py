input = input("Enter weight height separated by commas: ")
input_list = input.split(',')
print('input_list:%s' %str(input_list))
results = []
results = list(map(int ,input_list))
print(results)
dups = [x for x in results if results.count(x) > 1]
if len(dups) == 3:
	print('equilateral')
elif len(dups) == 2:
	print('isosceles')
else:
	print('scalene')