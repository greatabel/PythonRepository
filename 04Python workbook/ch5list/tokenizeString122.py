#(1+2*3)/-3+4
def tokenList(s):

	s = s.replace(" ","")
	tokens = []
	i = 0
	while i < len(s):
		# print(s)
		# handle the tokens / * ( )
		if s[i] == "*" or s[i] == "/" or s[i] == "^" or \
		   s[i] == "(" or s[i] == ")":
			tokens.append(s[i])
			i = i + 1
			# print("i=",i,"s[i-1]=",s[i-1])
		# + -
		elif s[i] == "+" or s[i] == "-":
			print("i=",i,"s[i-1]=",s[i-1])
			#前一个字符是数字或者括号
			if i > 0 and (s[i-1] >= "0" and s[i-1] <= "9" or s[i-1]== ")"):
				tokens.append(s[i])
				i = i + 1
			else:
				#属于数字
				num = s[i]
				i = i + 1

			#加上数字
				while i < len(s) and s[i] >= "0" and s[i] <= "9":
					num = num + s[i]
					i = i + 1
				tokens.append(num)
		#处理没有＋，－的数字
		elif s[i] >= "0" and s[i] <= "9":
			print("here=",s[i])
			num = ""
			while i < len(s) and s[i] >= "0" and s[i] <= "9":
					num = num + s[i]
					i = i + 1
			tokens.append(num)
			print('i=',i,"s[i]=",s[i])
		else:
			#返回错误
			return []
	return tokens

def main():
	
	s = input("Enter math express(blank line to quit):")
	while s !="":
		tokens = tokenList(s)
		print("tokens=",tokens)
		

		s = input("Enter sentences(blank line to quit):")

	
	

        
if __name__ == "__main__":
    main()