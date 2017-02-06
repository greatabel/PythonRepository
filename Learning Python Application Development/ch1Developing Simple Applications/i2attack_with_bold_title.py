import random
import textwrap


def main():
    keep_playing = 'y'

    occupants = ['enemy', 'friend', 'unoccupied']

    width = 72
    dotted_line = '-' * width
    print(dotted_line)
    print("\033[1m" + "Attack of The Orcs v0.0.1;" + "\033[0m")
    for i in range(0,10):
        print(random.choice(occupants))

if __name__ == "__main__":
    main()