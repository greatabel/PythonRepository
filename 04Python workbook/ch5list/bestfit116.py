import random
def bestFit(xlist,ylist):
	xAverage = sum(xlist)/len(xlist)
	yAverage = sum(ylist)/len(ylist)
	sm = 0
	smOfX2 = 0

	for i in range(0,len(xlist)):
		sm += xlist[i]*ylist[i]
		smOfX2 += xlist[i]**2 

	m = (sm - sum(xlist)*sum(ylist)/len(xlist) )/( smOfX2 - sum(xlist)**2 / len(xlist) )
	b = yAverage - m*xAverage

	finalEquation = str(m)+"x + "+str(b)
	return finalEquation

def main():
	
	xLine = input("Enter x list (blank line to quit):")
	yLine = input("Enter y list (blank line to quit):")
	xlist = []
	ylist = []
	for x in xLine.split(','):
		xlist.append(float(x))
	for y in yLine.split(','):
		ylist.append(float(y))
	if(len(xlist) == len(ylist)):
		print("bestFit(xlist,ylist)=",bestFit(xlist,ylist))


	
	

        
if __name__ == "__main__":
    main()