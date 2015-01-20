import sys
def get_input(msg):
	while True:
		try:
			line = input(msg)
			return int(line)
		except:
			# print("unexpected error:",sys.exc_info()[0])
			return None

#增加排序功能，为取中位数
def insertion_sort(items):
	for i in range(1,len(items)):
		j = i
		while j > 0 and items[j] < items[j-1]:
			items[j],items[j-1] = items[j-1],items[j]
			j -= 1

#变量			
inputDataArray = []
count = 0
sum = 0
lowest = 0
highest = 0
mean = 0
#中位数
middle =0
while True:
	data = get_input("enter a number or Enter to finish:")
	if  data is not None:
		inputDataArray.append(data)
		sum += data
		count += 1
	else:
		break
		
print('before sort:')
print('number:['+','.join(map(str,inputDataArray))+']')
print('after sort:')
insertion_sort(inputDataArray)
print('number:['+','.join(map(str,inputDataArray))+']')
if(len(inputDataArray)%2 ==1):
 middle = inputDataArray[len(inputDataArray)//2 +1]
else:
 middle = (inputDataArray[len(inputDataArray)//2]+inputDataArray[len(inputDataArray)//2 -1])/2
print('middle='+str(middle))

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

