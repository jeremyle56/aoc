import math


def find_distance(u, v):
    return math.fabs(u[0] - v[0]) + math.fabs(u[1] - v[1])


###############################################################################


def solve(expand_rate):
    galaxies = []

    row = 0
    col = 0
    for i in range(len(lines)):
        if i in dup_rows:
            row += expand_rate
        col = 0
        for j in range(len(lines[0])):
            if j in dup_cols:
                col += expand_rate
            if lines[i][j] == "#":
                galaxies.append((row, col))
            col += 1
        row += 1

    res = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            res += find_distance(galaxies[i], galaxies[j])

    return int(res)


###############################################################################


lines = open("input.txt").read().splitlines()

dup_rows = set()
dup_cols = set()

for i, row in enumerate(lines):
    if row.count("#") == 0:
        dup_rows.add(i)

for j in range(len(lines[0])):
    hasGalaxy = False
    for i in range(len(lines)):
        if lines[i][j] == "#":
            hasGalaxy = True
            break
    if not hasGalaxy:
        dup_cols.add(j)

print(f"Answer for Part 1: {solve(1)}")
print(f"Answer for Part 1: {solve(1000000 - 1)}")
