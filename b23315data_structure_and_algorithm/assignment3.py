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
            if available in [2, 3]:
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
        else:
            # use 50% to make dinner or breakfeast to be order from restaurants
            if random.randint(0, 1) == 0:
                breakfeast.append(5)
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


class Node:
    def __init__(self, sub="", children=None):
        self.sub = sub
        self.ch = children or []


class SuffixTree:
    def __init__(self, str):
        self.nodes = [Node()]
        for i in range(len(str)):
            self.addSuffix(str[i:])

    def addSuffix(self, suf):
        n = 0
        i = 0
        while i < len(suf):
            b = suf[i]
            x2 = 0
            while True:
                children = self.nodes[n].ch
                if x2 == len(children):
                    # no matching child, remainder of suf becomes new node
                    n2 = len(self.nodes)
                    self.nodes.append(Node(suf[i:], []))
                    self.nodes[n].ch.append(n2)
                    return
                n2 = children[x2]
                if self.nodes[n2].sub[0] == b:
                    break
                x2 = x2 + 1

            # find prefix of remaining suffix in common with child
            sub2 = self.nodes[n2].sub
            j = 0
            while j < len(sub2):
                if suf[i + j] != sub2[j]:
                    # split n2
                    n3 = n2
                    # new node for the part in common
                    n2 = len(self.nodes)
                    self.nodes.append(Node(sub2[:j], [n3]))
                    self.nodes[n3].sub = sub2[j:]  # old node loses the part in common
                    self.nodes[n].ch[x2] = n2
                    break  # continue down the tree
                j = j + 1
            i = i + j  # advance past part in common
            n = n2  # continue down the tree

    """
    The match succeeds exactly comparing the P.length sub-character. 
    And locating the child pointer of the node, similar to the Trie case, 
    if the number of alphabet is d. The query efficiency is O(d*m), i
    n fact, d is a fixed constant, and if the Hash table is used to locate directly, d=1.
      Therefore, the time complexity of querying the substring P of the suffix tree is O(m), 
      where m is the length of P
    total is O(N + M )
   
    """

    def max_repeats(self):
        results = []
        # tree nodes -> child
        child = []
        for i in range(len(self.nodes)):
            for j in self.nodes[i].ch:
                child.append((i, j))

        # nodes depths -> depth
        def get_depth(self, c, n):
            for i, j in child:
                if j == n:
                    c += len(self.nodes[j].sub)
                    if i == 0:
                        return c
                    else:
                        return get_depth(self, c, i)

        depth = {}
        inter = []
        for n in range(1, len(self.nodes)):
            if "$" not in self.nodes[n].sub:
                if len(self.nodes[n].ch) >= 2:
                    inter.append(n)
        for n in inter:
            depth[n] = get_depth(self, 0, n)

        # max depth -> max repeats
        def bottom_up(self, s, n):
            for i, j in child:
                if j == n:
                    if i == 0:
                        return s
                    else:
                        s = self.nodes[i].sub + s
                        return bottom_up(self, s, i)

        x = "a"
        for m in depth:
            if depth[m] >= 5:
                s = self.nodes[m].sub
                out = bottom_up(self, s, m)
                if out not in x:
                    x = out
                    results.append(out)
                    # print(out)
                else:
                    x = out
        return results


def compare_subs(submission1, submission2):
    t = submission1 + submission2 + "$"
    # print(t)
    common = SuffixTree(t).max_repeats()
    max_len = 0
    choose = ''
    for item in common:
        if len(item) >= max_len:
            max_len = len(item)
            choose = item
    print(max_len, choose, '#'*10)
    lenc = len(choose)
    len1 = len(submission1)
    len2 = len(submission2)
    rate1 = lenc / len1
    rate2 = lenc / len2

    print(choose, str(round(rate1, 2) * 100), str(round(rate2, 2) * 100))


def similarity_detector():
    submission1 = "radix sort and counting sort are both non comparison sorting algorithms"
    submission2 = "counting sort and radix sort are both non comparison sorting algorithms"
    compare_subs(submission1, submission2)


def main():
    print("-" * 10, "sharing_the_meal", "-" * 10)
    sharing_the_meal()

    print("\n\n")
    print("-" * 10, "similarity_detector", "-" * 10)
    similarity_detector()


if __name__ == "__main__":
    main()
