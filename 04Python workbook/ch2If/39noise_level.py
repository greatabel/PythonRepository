my_dict = {'Jackhammer': 130, 'Gas lawnmower': 106,
 'Alarm clock':70, 'Quiet room': 40}

iN = input("enter your thing's noise? ")
# print(iN)
if  iN in my_dict.keys():
	print('noise level is %d' %my_dict[iN])
else:
	try:
		num = int(iN)
		if num > 130:
			print("bigger than Jackhammer")
		elif num >106 and num < 130:
			print("less than Jackhammer ,bigger than gas lawnmower")
		elif num > 70 and num < 106:
			print('less than gas lawnmower, bigger than Alarm clock')
		elif num > 40 and num < 70:
			print('less than Alarm clock , bigger than Quiet room')
		elif num < 40:
			print('less than Quiet room')
	except ValueError:
		print("no valid integer")
	except:
		print("unexpetecd")
		raise
