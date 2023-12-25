import sys

sys.setrecursionlimit(1000000)


def get_neighbours_part1(x, y):
    neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    if trail[x][y] == ">":
        neighbours = [(x, y + 1)]
    elif trail[x][y] == "v":
        neighbours = [(x + 1, y)]
    elif trail[x][y] == "<":
        neighbours = [(x, y - 1)]
    elif trail[x][y] == "^":
        neighbours = [(x - 1, y)]

    return [(nx, ny) for nx, ny in neighbours if trail[nx][ny] != "#"]


def get_neighbours_part2(x, y):
    neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(nx, ny) for nx, ny in neighbours if trail[nx][ny] != "#"]


def dfs(x, y, visited, part2=False):
    if (x, y) == end:
        return len(visited)

    neighbours = get_neighbours_part2(x, y) if part2 else get_neighbours_part1(x, y)

    res = 0
    for n in neighbours:
        a, b = n
        if n in visited:
            continue

        visited.add(n)
        val = dfs(a, b, visited, part2)
        res = max(res, val)
        visited.remove(n)

    return res


###############################################################################


def solve_p1():
    return dfs(start[0], start[1], set())


###############################################################################


def solve_p2():
    return dfs(start[0], start[1], set(), True)


###############################################################################

input_file = "test.txt" if "test" in sys.argv else "input.txt"
lines = open(input_file).read().splitlines()

trail = [list(a) for a in lines]
MAX_ROW = len(trail)
MAX_COL = len(trail[0])

start = (0, 1)
end = (MAX_ROW - 1, MAX_COL - 2)

print(f"Answer for Part 1: {solve_p1()}")
print(f"Answer for Part 2: {solve_p2()}")
