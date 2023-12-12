from functools import cache


@cache
def getArrangements(spring, group, pos, cur_count, total_count):
    if pos == len(spring):
        return 1 if len(group) == total_count else 0
    elif spring[pos] == "#":
        return getArrangements(spring, group, pos + 1, cur_count + 1, total_count)
    elif spring[pos] == "." or total_count == len(group):
        if total_count < len(group) and cur_count == group[total_count]:
            return getArrangements(spring, group, pos + 1, 0, total_count + 1)
        elif cur_count == 0:
            return getArrangements(spring, group, pos + 1, cur_count, total_count)
        else:
            return 0

    hash = getArrangements(spring, group, pos + 1, cur_count + 1, total_count)
    dot = 0
    if cur_count == group[total_count]:
        dot = getArrangements(spring, group, pos + 1, 0, total_count + 1)
    elif cur_count == 0:
        dot = getArrangements(spring, group, pos + 1, cur_count, total_count)
    return hash + dot


###############################################################################


def solve_p1():
    springs = [i.split()[0] + "." for i in lines]
    groups = [[int(i) for i in j.split()[1].split(",")] for j in lines]

    res = 0

    for i in range(len(lines)):
        res += getArrangements(springs[i], tuple(groups[i]), 0, 0, 0)

    print(f"Answer for Part 1: {res}")


###############################################################################


def solve_p2():
    springs = [i.split()[0] for i in lines]
    temp = []
    for i in range(len(springs)):
        spring = []
        for _ in range(5):
            spring.append(springs[i])
        temp.append(spring)

    springs = ["?".join(i) + "." for i in temp]
    groups = [[int(i) for i in j.split()[1].split(",")] * 5 for j in lines]

    res = 0

    for i in range(len(lines)):
        res += getArrangements(springs[i], tuple(groups[i]), 0, 0, 0)

    print(f"Answer for Part 2: {res}")


###############################################################################


lines = open("input.txt").read().splitlines()

solve_p1()
solve_p2()
