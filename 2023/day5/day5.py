import collections, math, sys, re

###############################################################################


def solve_p1():
    seedsMap = dict((i, i) for i in seeds)
    moved = dict((i, False) for i in seeds)

    for line in lines:
        if re.match(r"[^0-9 ]", line):
            moved = dict.fromkeys(moved, False)
            continue

        line = [int(i) for i in line.split()]
        [dest, src, length] = line

        for key, value in seedsMap.items():
            if value >= src and value < src + length and not moved[value]:
                seedsMap[key] = dest + (value - src)
                moved[dest + (value - src)] = True

    print(f"Answer for Part 1: {min(seedsMap.values())}")


###############################################################################


def solve_p2():
    seedsRange = [seeds[i : i + 2] for i in range(0, len(seeds), 2)]

    seedsMap = []
    for [start, length] in seedsRange:
        for i in range(start, start + length):
            seedsMap.append(i)

    reverse = lines
    reverse.reverse()

    loc = 10000000
    moved = False
    currPos = 0

    while True:
        for line in reverse:
            if re.match(r"[^0-9 ]", line):
                moved = False
                continue

            line = [int(i) for i in line.split()]
            [dest, src, length] = line
            if currPos >= dest and currPos < dest + length and not moved:
                currPos = src + (currPos - dest)
                moved = True

        if currPos in seedsMap or loc == 88151870:
            break
        else:
            loc += 1
            moved = False
            currPos = loc

    print(f"Answer for Part 2: {loc}")


###############################################################################


lines = open("input.txt").read().splitlines()
seeds = [int(i) for i in lines[0].split(": ")[1].split()]

lines = [i for i in lines[1:] if i.strip()]

solve_p1()
solve_p2()
