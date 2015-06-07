#http://stackoverflow.com/questions/12797067/how-can-i-do-a-1-b-in-python
def get_input(msg):
		try:
			line = input(msg)
			
			return line
		except:
			# print("unexpected error:",sys.exc_info()[0])
			return None

# import calendar
yearastro = {0:"Monkey",1:"Rooster",2:"Dog",3:"Pig",
4:"Rat",5:"Ox",6:"Tiger",7:"Hare",8:"Dragon",9:"Snake",
10:"Horse",11:"Sheep"} 

def to_dict(name): 
	return month_dict[name] 

while True:
	iN = get_input("input year (enter 'enter' to exit): ")
	if  iN is not None and iN!="":
		
		try:
			myyear = int(iN)%12
			if(myyear in yearastro.keys()):
				print(yearastro[myyear])
			
			
		except:
			print('error input')
			# break
	else:
		break