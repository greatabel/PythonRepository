K = 3
line = input("Enter word:")
import math

alphabet = list('abcdefghijklmnopqrstuvwxyz')
while line != "":
	cipher = ""
	for c in line:
		if c in alphabet:
			cipher += alphabet[(alphabet.index(c)+K)%len(alphabet)]
	print("after encryped =", cipher)
	line = input("Enter word:") 

