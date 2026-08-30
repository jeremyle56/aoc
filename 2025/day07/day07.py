import sys
from collections import defaultdict

###############################################################################


def solve_p1():
    res = 0
    split = set()
    split.add(locS)
    for i in range(1, len(lines)):
        temp = set()
        for j in split:
            if lines[i][j] == "^":
                if j - 1 >= 0:
                    temp.add(j - 1)
                if j + 1 < len(lines[0]):
                    temp.add(j + 1)
                res += 1
            else:
                temp.add(j)
        if len(temp) != 0:
            split = temp

    return res


def solve_p2():
    large_thing = defaultdict(int)
    large_thing[locS] = 1
    split = set()
    split.add(locS)
    for i in range(1, len(lines)):
        temp = set()
        for j in split:
            if lines[i][j] == "^":
                if j - 1 >= 0:
                    temp.add(j - 1)
                    large_thing[j - 1] += large_thing[j]
                if j + 1 < len(lines[0]):
                    temp.add(j + 1)
                    large_thing[j + 1] += large_thing[j]
                large_thing[j] = 0
            else:
                temp.add(j)
        if len(temp) != 0:
            split = temp

    res = 0
    for i in large_thing:
        res += large_thing[i]

    print(large_thing)
    return res


###############################################################################

lines = open("in.txt").read().splitlines()

locS = 0
for i in range(len(lines[0])):
    if lines[0][i] == "S":
        locS = i
        break


print(f"Answer for Part 1: {solve_p1()}")
print(f"Answer for Part 2: {solve_p2()}")
