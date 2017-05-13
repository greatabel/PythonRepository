#http://outofmemory.cn/code-snippet/5011/Python-jinzhi-together-switch-two-jinzhi-shi-jinzhi-shiliu-jinzhi
import math
def  hex2int(s):
	result = 0
	i = 0
	for c in s.lower():
		myint = 0
		if c.isdigit():
			myint = int(c)
		elif ord(c) - ord('a') <=5:
			myint = 10 + (ord(c) - ord('a'))
		print(myint)
		i += 1
		result += myint * pow(16,len(s) - i)
	return result

# global definition
# base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]

def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])

def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def main():
	while True:
		line = input("hex:")
		if is_hex(line):
			print("Your random pass is:", hex2int(line))
			break
		else:
			print("not hex")

	print("int to hex!")
	while True:
		line = int(input("int:"))
		print(dec2hex(line))
		break

if __name__ == "__main__":
	main()
