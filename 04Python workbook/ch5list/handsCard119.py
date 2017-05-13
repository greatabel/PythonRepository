from  shufflingCard118 import createCards,shuffleCards

def deal(numOfhand, numPerhand, cards):
	roundNum = len(cards)//(numPerhand * numOfhand)
	for i in range(roundNum):
		print("turn",cards[:numOfhand * numPerhand])
		cards = cards[numPerhand * numOfhand:]
	print("remain:",cards[0:])


def main():
	
	cards = createCards()
	cards = shuffleCards(cards)
	deal(2,5,cards)

	
	

        
if __name__ == "__main__":
    main()