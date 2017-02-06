import random
import textwrap


def main():
    keep_playing = 'y'

    occupants = ['enemy', 'friend', 'unoccupied']

    width = 72
    dotted_line = '-' * width
    print(dotted_line)
    print("\033[1m" + "Attack of The Orcs v0.0.1;" + "\033[0m")

    msg = (
    "The war between humans and their arch enemies, Orcs, was in the "
    "offing. Sir Foo, one of the brave knights guarding the southern "
    "plains began a long journey towards the east through an unknown "
    "dense forest. On his way, he spotted a small isolated settlement."
    " Tired and hoping to replenish his food stock, he decided to take"
    " a detour. As he approached the village, he saw five huts. There "
    "was no one to be seen around. Hesitantly, he  decided to enter..")

    print(msg)

    for i in range(0,10):
        print(random.choice(occupants))

if __name__ == "__main__":
    main()