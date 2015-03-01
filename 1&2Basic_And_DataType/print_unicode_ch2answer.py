import sys
import unicodedata
def print_unicode_table(word):
	print("decimal hex chr {0:^40}".format("name"))
	print("--- --- {0:-<40}".format(""))

	code = ord(" ")
	end = sys.maxunicode

	while code < end:
		c = chr(code)
		name = unicodedata.name(c,"*** unknown ***")
		flag = False
		for arg in word:
			if arg.lower() in name.lower():
				flag = True
			else:
				flag = False
				break

		if  flag:
			# print('{0:^3c} '.format(code))
			try:
				print("{0:7} {0:5X} {0:^3c} {1}".format(code,name.title()))
			except:
				print("Error in print_unicode_table")
		code += 1

word = None
if len(sys.argv) >1:
	if sys.argv[1] in ("-h","--help"):
		print("usage:{0}[string]".format(sys.argv[0]))
		word = 0
	else:
		word = sys.argv[1:]
if word !=0 and word!=None and len(word)>0:
	print("{0} is word".format(word))
	print_unicode_table(word)
