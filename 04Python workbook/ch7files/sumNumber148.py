# import sys
# sys.path.insert(0,'../ch5list')
# from onlywords111 import findwords

def main():
	# import calendar
	LetterToPoint = {"A+":4.0,"A":4.0,"A-":3.7,
	"B+":3.3, "B":3.0,"B-":2.7 } 



	while True:
		iN = input("input Letter of point (enter 'enter' to exit): ")
		if  iN is not None and iN!="":
			iN = iN.upper()
			try:
				if(iN in LetterToPoint.keys()):
					print(LetterToPoint[iN])
				else:
					print("don't know")
				
			except:
				print('error input')
				# break
		else:
			break


        
if __name__ == "__main__":
    main()