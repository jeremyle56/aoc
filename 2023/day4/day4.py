import collections, math, sys, re

###############################################################################


def solve_p1():
    res = sum(2 ** (i - 1) for i in winnings if i > 0)

    print(f"Answer for Part 1: {res}")


###############################################################################


def solve_p2():
    cards = dict((i, 1) for i in range(1, len(lines) + 1))

    for i in range(1, len(cards)):
        for j in range(1, winnings[i - 1] + 1):
            cards[i + j] += cards[i]

    print(f"Answer for Part 2: {sum(cards.values())}")


###############################################################################


lines = open("input.txt").read().splitlines()
lines = [re.sub(" +", " ", i).split(": ")[1].split(" | ") for i in lines]
lines = [[set([int(k) for k in j.split(" ")]) for j in i] for i in lines]
winnings = [len(i[0] & i[1]) for i in lines]

solve_p1()
solve_p2()
