import random

"""

loop is n
the inner is just 5, is N
choice is random , so is less than N
n*5+n*n is O(n*2)
"""


def allocate(availability):
    breakfeast = []
    dinner = []
    for day_th, availability_per_day in enumerate(availability):
        b_choices = []
        d_choices = []
        for idx_th_p, available in enumerate(availability_per_day):
            # print(idx_th, available)
            # mean  only time for breakfeast
            if available in [1, 3]:
                b_choices.append(idx_th_p)
            # mean  only time for dinner
            if available in [2, 3] and (idx_th_p not in breakfeast):
                d_choices.append(idx_th_p)

        if len(b_choices) == 0:
            b_choices.append(5)
        if len(d_choices) == 0:
            d_choices.append(5)
        # make it as equal as prosillble
        b = random.choice(b_choices)
        d = random.choice(d_choices)
        if b != d:
            breakfeast.append(b)
            dinner.append(d)
        print(day_th, "day ---", b_choices, "#" * 5, d_choices, "-" * 5, b, d)

    # d = ([3, 2, 1, 4, 0, 2, 3, 2, 2, 3], [4, 0, 3, 2, 5, 4, 1, 1, 3, 0])
    results = (breakfeast, dinner)
    return results


def sharing_the_meal():

    # Example
    availability = [
        [2, 0, 2, 1, 2],
        [3, 3, 1, 0, 0],
        [0, 1, 0, 3, 0],
        [0, 0, 2, 0, 3],
        [1, 0, 0, 2, 1],
        [0, 0, 3, 0, 2],
        [0, 2, 0, 1, 0],
        [1, 3, 3, 2, 0],
        [0, 0, 1, 2, 1],
        [2, 0, 0, 3, 0],
    ]
    r = allocate(availability)
    print(r)


def similarity_detector():
    """"""


def main():
    print("-" * 10, "sharing_the_meal", "-" * 10)
    sharing_the_meal()
    print("-" * 10, "similarity_detector", "-" * 10)
    similarity_detector()


if __name__ == "__main__":
    main()
