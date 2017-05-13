#只是例子，不想打太多
NUMBER_WORDS = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety"
}


def NumbersInEnglish(theDict,n):
	import math
	print('theinput=',n)
	inputStr = ''
	
	thousands = n//1000
	hundreds = (n // 100 ) % 10
	ones = n % 10
	tens = n % 100

	print(ones,tens,hundreds,thousands)

	if thousands:
		inputStr += str(thousands) +' thousands '
	if hundreds:
		inputStr += str(hundreds) + ' hundreds '
	if tens:
		if tens in NUMBER_WORDS.keys():
			#像是 20下
			inputStr += NUMBER_WORDS[tens]
		else:
			ten10 = (tens // 10 ) * 10
			ten1  = (tens % 10)
			# print('ten',ten10,ten1)
			inputStr += ( NUMBER_WORDS[ten10] + ' and ' + NUMBER_WORDS[ten1])

	return inputStr
	# return returnlist

def main():
	
	theinput = input("Enter the message (like G2G blank line to quit):")

	

	while theinput!="":
		
		theinput = int(theinput)
		theResult = NumbersInEnglish(NUMBER_WORDS,theinput)
		print('theResult ','-'*20)
		print(theResult)

		theinput = input("Enter the value you want to reverse loop (blank line to quit):")

       
if __name__ == "__main__":
    main()
