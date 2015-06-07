#http://stackoverflow.com/questions/12797067/how-can-i-do-a-1-b-in-python
def get_input(msg):
		try:
			line = input(msg)
			
			return line
		except:
			# print("unexpected error:",sys.exc_info()[0])
			return None
ilist = []
# 4e12 输入例子
while True:

	iNum = get_input("input number plate (enter 'enter' to exit): ")
	if len(ilist)==0 and iNum == '0':
		print('frist input should not be 0')
	else:
		if iNum is not None and iNum !="" and iNum!='0' :
			iNum = float(iNum)
			ilist.append(iNum)
		else:
			break
print(sum(ilist))
