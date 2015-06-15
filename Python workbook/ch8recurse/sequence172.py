#不明白题意

def loadNames():
	return ["Ab","Bc","Cc","Cddd","Cx","Ct","Dd","Ditest"]

def longestSequece(start,words):
	if start == "":
		return []

	best = []
	last_letter = start[len(start) -1].lower()
	for i in range(0,len(words)):
		first_letter = words[i][0].lower()
		if first_letter == last_letter:
			candidate = longestSequece(words[i],\
				words[0:i]+ words[i+1: len(words)])
			if len(candidate) > len(best):
				best = candidate
	return [start]+best

def main():
	names = loadNames()
	start = "Ab"
	start = start.capitalize()

	names.remove(start)
	sequence = longestSequece(start, names)
	print(sequence)

if __name__ == "__main__":
    main()



