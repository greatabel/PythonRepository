from i6answer_clickcounter import Counter

def main():
    myCounter = Counter()
    myCounter.add()
    myCounter.add()
    print(myCounter.show())
    myCounter.reset()
    print(myCounter.show())


if __name__ == "__main__":
    main()