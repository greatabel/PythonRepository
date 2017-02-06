import random


def main():
    occupants = ['enemy', 'friend', 'unoccupied']
    for i in range(0,10):
        print(random.choice(occupants))

if __name__ == "__main__":
    main()