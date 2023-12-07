import collections, math, sys, re


def determine_rank(cards):
    if "J" in cards:
        return determine_rank_j(cards)

    if len(set(cards) & set(types)) == 1:
        return "Five"
    elif len(set(cards) & set(types)) == 2:
        cards_set = set(cards)
        for card in cards_set:
            if cards.count(card) == 4:
                return "Four"
        return "Full"
    elif len(set(cards) & set(types)) == 3:
        cards_set = set(cards)
        for card in cards_set:
            if cards.count(card) == 3:
                return "Three"
        return "Two"
    elif len(set(cards) & set(types)) == 4:
        return "One"
    else:
        return "High"


def determine_rank_j(cards):
    if cards.count("J") == 5:
        return "Five"

    most_common = collections.Counter(cards.replace("J", "")).most_common(1)[0][0]
    temp = cards.replace("J", most_common)

    return determine_rank(temp)


# Insert position
def insert_to_ranking(rankings, line):
    for i in range(len(rankings)):
        if compare_two(rankings[i][0], line[0]):
            rankings.insert(i, line)
            return
    rankings.append(line)


# Return true if cards1 belongs after cards2
def compare_two(cards1, cards2):
    for i in range(5):
        if cards1[i] != cards2[i]:
            return types.index(cards1[i]) > types.index(cards2[i])


###############################################################################


def solve_p2():
    five = []
    four = []
    full = []
    three = []
    two = []
    one = []
    high = []

    for line in lines:
        cards = line[0]
        rank = determine_rank(cards)
        if rank == "Five":
            insert_to_ranking(five, line)
        elif rank == "Four":
            insert_to_ranking(four, line)
        elif rank == "Full":
            insert_to_ranking(full, line)
        elif rank == "Three":
            insert_to_ranking(three, line)
        elif rank == "Two":
            insert_to_ranking(two, line)
        elif rank == "One":
            insert_to_ranking(one, line)
        else:
            insert_to_ranking(high, line)

    ranking = five + four + full + three + two + one + high
    ranking.reverse()
    ranking = list(enumerate(ranking, start=1))

    print(f"Answer for Part 2: {sum(i[0] * i[1][1] for i in ranking)}")


###############################################################################


lines = open("input.txt").read().splitlines()
lines = [i.split() for i in lines]
lines = [[i, int(y)] for i, y in lines]

types = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

solve_p2()
