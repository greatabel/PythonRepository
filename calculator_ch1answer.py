import sys
def get_input(msg):
	while True:
		try:
			line = input(msg)
			return int(line)
		except:
			# print("unexpected error:",sys.exc_info()[0])
			return None

inputDataArray = []
count = 0
sum = 0
lowest = 0
highest = 0
mean = 0

while True:
	data = get_input("enter a number or Enter to finish:")
	if  data is not None:
		inputDataArray.append(data)
		sum += data
		count += 1
	else:
		break

print('number:['+','.join(map(str,inputDataArray))+']')
print('count = '+str(count)+' sum = '+str(sum), end = " ")

lowest = inputDataArray[0]
highest = inputDataArray[0]
for element in inputDataArray[1:]:
	if element < lowest:
		lowest = element
	else:
		highest = element

mean = sum /count
print('lowest='+str(lowest)+' highest='+str(highest)+' mean='+str(mean))