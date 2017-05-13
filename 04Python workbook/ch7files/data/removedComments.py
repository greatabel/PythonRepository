
def main():
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
		else:
			break

        
if __name__ == "__main__":
    main()

