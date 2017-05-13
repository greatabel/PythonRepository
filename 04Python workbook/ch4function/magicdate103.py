from daysInMonth100 import findDaysOfMonth

def isMagicDate(day,month ,year):
	if day * month == year % 100:
		return True
	else:
		return False

def main():
	count = 0
	for year in range(1900, 2000):
		for month in range(1,13):
			for day in range(1, findDaysOfMonth(month, year)):
				if isMagicDate(day,month,year):
					count += 1
					print("day %02d month %02d year %04d is a magic date" %(day, month, year))
	print("count=",count)

if __name__ == "__main__":
	main()