# -*- coding: utf-8 -*-
#使用方式：python3 statistics_ch3.py test_statistics_ch3.txt 

import sys
import collections

Statistics = collections.namedtuple("Statistics", "mean mode median std_dev")

def read_data(filename, numbers, frequencies):
	for lino,line in enumerate(open(filename, encoding="ascii"), start=1):
		for x in line.split():
			try:
				number = float(x)
				numbers.append(number)
				frequencies[number]+=1
			except ValueError as err:
				print("{filename}:{lino}: skipping {x}:{err}".format(
					 **locals()))

def calculate_mode(frequencies,maximum_modes):
	highest_frequency = max(frequencies.values())
	mode = [number for number ,frequency in frequencies.items()
	if frequency == highest_frequency]
	if not (1 <=len(mode) <=maximum_modes):
		mode = None
	else:
		mode.sort()
	return mode

def calculate_median(numbers):
	numbers = sorted(numbers)
	middle = len(numbers)//2
	median = numbers[middle]
	if len(numbers)%2 == 0:
		median = (median + numbers[middle -1])/2
	return median

import math
def calculate_std_dev(numbers, mean):
	total = 0
	for number in numbers:
		total +=((number - mean)**2)
	variance = total/(len(numbers) -1)
	return math.sqrt(variance)

def print_results(count,Statistics):
	real = "9.2f"
	if Statistics.mode is None:
		modeline =""
	elif len(Statistics.mode) ==1:
		modeline = "mode ={0:{fmt}}\n".format(
			Statistics.mode[0],fmt=real)
	else:
		modeline = ("mode =["+
			",".join(["{0:.2f}".format(m)
				for m in Statistics.mode])+"]\n")
	print("""\, 
		count = {0:6}
		mean  = {mean:{fmt}}
		median= {median:{fmt}}
		{1}\
		std.dev. ={std_dev:{fmt}}""".format(
			count,modeline,fmt=real,**Statistics._asdict()))
def calculate_statistics(numbers, frequencies):
	mean = sum(numbers)/len(numbers)
	mode = calculate_mode(frequencies,3)
	median = calculate_median(numbers)
	std_dev = calculate_std_dev(numbers,mean)
	return Statistics(mean,mode,median,std_dev)


def main():
	print("test")
	if len(sys.argv) == 1 or sys.argv[1] in {"-h","--help"}:
		print("usage:{0} file1 [file2[...fileN]]".format(
			sys.argv[0]))
		sys.exit()

	numbers =[]
	frequencies = collections.defaultdict(int)
	for filename in sys.argv[1:]:
		read_data(filename, numbers,frequencies)
	if numbers:
		Statistics = calculate_statistics(numbers,frequencies)
		print_results(len(numbers),Statistics)
	else:
		print("no numbers found")

main()




