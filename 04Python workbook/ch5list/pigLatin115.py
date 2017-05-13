#官方答案是错误的
def piglatin(s):
	
	vowels = ['a','e','i','o','u']
	marks = [':','.','!','?']
	words = s.split(" ")
	newwords = []
	for word in words:
		mark = ''
		if word[len(word)-1] in marks:
			mark = word[len(word)-1]
			word = word[:len(word)-1]

		if word[0] in vowels:
			newword = word[0]+'way'
		else:
			newword = word[1:]+'ay'
		if mark != '':
			newword = newword+mark
		newwords.append(newword.title())
	return ' '.join(str(x) for x in newwords)

def main():
	
	s = input("Enter sentences(blank line to quit):")
	while s != "":
		print(piglatin(s))
	
		s = input("Enter sentences(blank line to quit):")

	
	

        
if __name__ == "__main__":
    main()