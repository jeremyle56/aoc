import collections, math, sys, re


def calculate(line, rows):
    diffs = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    rows.append(diffs)
    if set(diffs) == {0}:
        return rows
    else:
        return calculate(diffs, rows)


###############################################################################


def solve_p1():
    res = 0
    for line in lines:
        rows = calculate(line, [line])
        for i in range(len(rows) - 1, 0, -1):
            rows[i - 1].append(rows[i - 1][-1] + rows[i][-1])
        res += rows[0][-1]

    print(f"Answer for Part 1: {res}")


###############################################################################


def solve_p2():
    res = 0
    for line in lines:
        rows = calculate(line, [line])
        for i in range(len(rows) - 1, 0, -1):
            rows[i - 1].insert(0, rows[i - 1][0] - rows[i][0])
        res += rows[0][0]

    print(f"Answer for Part 2: {res}")


###############################################################################


lines = open("input.txt").read().splitlines()
lines = [[int(i) for i in j.split()] for j in lines]

# solve_p1()
# solve_p2()

###############################################################################


def clean(l):
    diffs = [l[i + 1] - l[i] for i in range(len(l) - 1)]
    return l + [l[-1]] if set(diffs) == {0} else l + [l[-1] + clean(diffs)[-1]]


def part1():
    print(f"Answer for part 1 (clean): {sum(clean(line)[-1] for line in lines)}")


def part2():
    print(f"Answer for part 2 (clean): {sum(clean(line[::-1])[-1] for line in lines)}")


part1()
part2()
