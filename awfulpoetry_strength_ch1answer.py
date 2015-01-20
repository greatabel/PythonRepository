articles = ['the','a','another','other']
subjects = ['cat','dog','man','woman','boy']
verbs    = ['sang','ran','jumped','drank']
adverbials =['loudly','quietly','well','badly']

import random

import sys
def get_input(msg):
	while True:
		try:
			line = input(msg)
			return int(line)
		except:
			# print("unexpected error:",sys.exc_info()[0])
			return None


def makepoetry(linecount):		
	sentence = ''		
	for i in range(linecount):
		# print(i)
		sentence = ''
		myindex = random.randint(0,len(articles)-1)
		sentence += articles[myindex]+' '
		myindex = random.randint(0,len(subjects)-1)
		sentence += subjects[myindex]+' '
		myindex = random.randint(0,len(verbs)-1)
		sentence += verbs[myindex]+' '
		myindex = random.randint(0,len(adverbials)-1)
		sentence += adverbials[myindex]
		print(sentence)

while True:
	data = get_input("enter a number or Enter to finish:-->")
	if  data is not None:
		makepoetry(data)
	else:
		makepoetry(5)
		break

