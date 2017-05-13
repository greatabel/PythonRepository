#http://stackoverflow.com/questions/12797067/how-can-i-do-a-1-b-in-python
def get_input(msg):
		try:
			line = input(msg)
			
			return line
		except:
			# print("unexpected error:",sys.exc_info()[0])
			return None






# 4e12 输入例子
while True:
	plate = get_input("input license plate (enter 'enter' to exit): ")
	if  plate is not None and plate!="":
		if len(plate) == 6 and plate[0] >="A" and plate[0] <="Z" and \
			plate[1] >= "A" and plate[1] <="Z" and \
			plate[2] >= "A" and plate[2] <= "Z":
			print("valide style")
		else:
			print("not valid")
	else:
		break