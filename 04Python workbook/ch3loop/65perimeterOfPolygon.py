from math import sqrt

# def get_input(msg):
# 		try:
# 			line = input(msg)
			
# 			return line
# 		except:
# 			# print("unexpected error:",sys.exc_info()[0])
# 			return None

#-------- 第一点
perimeter = 0
frist_x  = input("input x (enter 'enter' to exit): ")
frist_y  = input("input y (enter 'enter' to exit): ")
if frist_x =="" or frist_y =="":
	print('error input')
else:
	frist_x = float(frist_x)
	frist_y = float(frist_y)

prev_x = frist_x
prev_y = frist_y

#------循环
while True:

	lineX  = input("input x (enter 'enter' to exit): ")
	lineY  = input("input y (enter 'enter' to exit): ")
	if lineX =="" or lineY =="":
		break
	else:
		x = float(lineX)
		y = float(lineY)


	if x is not None and x !="" and y is not None and y !="" :
		dist = sqrt((prev_x - x) ** 2 + (prev_y - y) ** 2 )
		perimeter = perimeter + dist
		print('perimeter=',perimeter)
		prev_x = x
		prev_y = y

	else:
		break
#－－－－－－连接第一点的边
dist = sqrt((frist_x - x) ** 2 + (frist_y - y) ** 2 )
perimeter = perimeter + dist

print("The perimeter of polygon is ", perimeter)