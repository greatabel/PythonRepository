#http://stackoverflow.com/questions/4938429/how-do-we-determine-the-number-of-days-for-a-given-month-in-python
def findDaysOfMonth(month,year):
	from calendar import monthrange
	result = monthrange(year, month)
	return result[1]

def main():
	line = input(" month,year :")
	ilist = line.split(",")
	month = int(ilist[0])
	year = int(ilist[1])

	print("the %d month has %d days" %( month , findDaysOfMonth(month,year) ))

if __name__ == "__main__":
	main()