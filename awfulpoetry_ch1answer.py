articles = ['the','a','another','other']
subjects = ['cat','dog','man','woman','boy']
verbs    = ['sang','ran','jumped','drank']
adverbials =['loudly','quietly','well','badly']

import random

sentence = ''
for i in range(5):
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


