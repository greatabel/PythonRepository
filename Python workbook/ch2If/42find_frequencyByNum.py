C4_FREQ = 261.63
D4_FREQ = 293.66
LIMIT = 1
freq = float(input('enter a frequency: '))

if freq > C4_FREQ - LIMIT and freq <= C4_FREQ + LIMIT:
	note = "C4"
elif freq >= D4_FREQ - LIMIT and freq <= D4_FREQ + LIMIT:
	note = "D4"
else:
	note = ""

if note == "" :
	print("don't know")
else:
	print("is ",note)