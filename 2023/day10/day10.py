import collections


def find_neighbours(u):
    [x, y] = u
    neighbours = []
    possible = dirs[lines[x][y]]

    for dx, dy in possible:
        if (-dx, -dy) in dirs[lines[x + dx][y + dy]]:
            neighbours.append((x + dx, y + dy))

    return neighbours


def dfs():
    res = 0

    s = [start]
    depth = [0]
    parent_map = {}
    visited = set()

    while len(s):
        u = s.pop()
        d = depth.pop()

        if u not in visited:
            visited.add(u)
            neighbours = find_neighbours(u)
            for v in neighbours:
                if v not in visited or v == start:
                    s.append(v)
                    depth.append(d + 1)
                    parent_map[toKey(v)] = toKey(u)
        res = max(depth + [res])

    return [res, parent_map]


def toKey(u):
    return str(u[0]) + " " + str(u[1])


def toTuple(u):
    u = [int(i) for i in u.split()]
    return (u[0], u[1])


def determine_start(start):
    neighbours = find_neighbours(start)
    neighbours = [(i[0] - start[0], i[1] - start[1]) for i in neighbours]

    for i in dirs.keys():
        if collections.Counter(dirs[i]) == collections.Counter(neighbours):
            return i
    return "0"


###############################################################################


def solve_p1():
    print(f"Answer for Part 1: {int(dfs()[0] / 2)}")


###############################################################################


def solve_p2():
    parent_map = dfs()[1]

    path = [start]
    curr = parent_map[toKey(start)]
    while curr != toKey(start):
        path.append(toTuple(curr))
        curr = parent_map[curr]

    mapping = [["0" for _ in range(MAX_COL)] for _ in range(MAX_ROW)]
    for i in range(MAX_ROW):
        for j in range(MAX_COL):
            if (i, j) in path:
                mapping[i][j] = lines[i][j]
    mapping[start[0]][start[1]] = determine_start(start)

    res = 0
    for i in range(MAX_ROW):
        for j in range(1, MAX_COL):
            if sum(1 for k in mapping[i][:j] if k in "LJ|") % 2 == 1:
                if mapping[i][j] == "0":
                    res += 1

    print(f"Answer for Part 2: {res}")


###############################################################################


lines = open("input.txt").read().splitlines()

dirs = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    ".": [],
    "S": [(0, 1), (1, 0), (0, -1), (-1, 0)],
}

MAX_ROW = len(lines)
MAX_COL = len(lines[0])

start = (0, 0)
for i in range(MAX_ROW):
    for j in range(MAX_COL):
        if lines[i][j] == "S":
            start = (i, j)
            break

solve_p1()
solve_p2()
