C4_FREQ = 261.63
D4_FREQ = 293.66

name = input('Enter 2 character note name ,such as C4: ')

note =name[0]
octave = int(name[1])

if note == 'C':
	freq = C4_FREQ
elif note == 'D':
	freq = D4_FREQ
else:
	print("don't know")

freq = freq/ 2 **(4 - octave)
print(" The freqency of ", name , "is ",freq)