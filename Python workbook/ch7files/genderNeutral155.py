import sys

def main():
	try:
		boylines = []
		girllines = []
		for i in range(2000,2013):
			filenameB = 'BabyNames/'+str(i)+"_BoysNames.txt"
			filenameG = 'BabyNames/'+str(i)+"_GirlsNames.txt"

			with open(filenameB) as infile:
				line = infile.readline().strip()
				boylines.append(line)
				print(line)

			with open(filenameG) as infile:
				line = infile.readline().strip()
				girllines.append(line)
				print('line=',line)




	except IOError:
		print("获取文件时候出错")
		quit()

	print("-"*20)
	print(boylines,'-'*30,girllines)
	# from sets import Set
	neutralList = set()
	neutralListG = set()
	for item in boylines:
		name = item.split(" ")
		if not name[0] in neutralList:
			neutralList.add(name[0])
	for item in girllines:
		name = item.split(" ")
		if not name[0] in neutralListG:
			neutralListG.add(name[0])
	neutralListTemp = neutralList.copy()
	print('*'*30)
	print(neutralList)
	print('*'*30)
	print(neutralListG)
	for item in neutralListTemp:
		if not item in neutralListG:
			neutralList.remove(item)



	print('neutralList=',neutralList)



	

	


	


        
if __name__ == "__main__":
    main()
