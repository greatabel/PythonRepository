import random
def createCards():
	colors=['红','黑','梅','方']
	values ='23456789IJQKA'
	cards = []
	for c in colors:
		for i in values:
			card = c + i
			cards.append(card)
	print(cards)
	print(len(cards))
	return cards

def shuffleCards(cards):
	beforecards = cards
	aftercards = []
	for i in range(len(cards)):
		randomCard = beforecards[random.randint(0,len(beforecards)-1)]
		print('randomCard=',randomCard)
		beforecards.remove(randomCard)
		aftercards.append(randomCard)
	print(aftercards)
	print(len(aftercards))
	return aftercards


def main():
	
	cards = createCards()
	shuffleCards(cards)


	
	

        
if __name__ == "__main__":
    main()