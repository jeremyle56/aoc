import collections, math, sys, re

###############################################################################


def solve_p1():
    res = 0
    for line in lines:
        line = re.sub(" +", " ", line)
        line = line.split(": ")[1].split(" | ")
        your_numbers = [int(i) for i in line[0].split(" ")]
        winning = [int(i) for i in line[1].split(" ")]
        matches = len(set(your_numbers) & set(winning))
        if matches > 0:
            res += 2 ** (matches - 1)

    print(f"Answer for Part 1: {res}")


###############################################################################


def solve_p2():
    cards = dict((i, 1) for i in range(1, len(lines) + 1))

    for line in lines:
        line = re.sub(" +", " ", line)
        card_num = int(line.split(" ")[1].split(":")[0])
        line = line.split(": ")[1].split(" | ")
        your_numbers = line[0].split(" ")
        winning = line[1].split(" ")
        matches = len(set(your_numbers) & set(winning))

        if matches > 0:
            for i in range(1, matches + 1):
                cards[card_num + i] += cards[card_num]

        print(cards)

    print(f"Answer for Part 2: {sum(cards.values())}")


###############################################################################


lines = open("input.txt").read().splitlines()
solve_p1()
solve_p2()
