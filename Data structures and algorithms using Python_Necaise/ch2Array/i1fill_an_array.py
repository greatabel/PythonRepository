from array import Array
import random

def main():
    valueList = Array(100)
    for i in range(len(valueList)):
        valueList[i] = random.random() * 100

    for value in valueList:
        print("#", value)

if __name__ == "__main__":
    main()