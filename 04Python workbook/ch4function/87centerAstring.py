def centerStr(s,mylength):
	returnS = ""
	if (len(s)>= mylength):
		returnS = s
	else:
		# padding = int( (mylength - len(s))/2)
		#  //operator divison truncated to integer
		padding = (mylength - len(s))//2
		returnS = " "*padding +s +" "*padding+"|"
	return returnS

def main():
	print(centerStr("hello",10))
	print(centerStr("hello world",50))
	print(centerStr("hello world",30))

main()
