import sys
from copy import deepcopy

DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def get_garden_plots(steps):
    prev = [[False for _ in range(MAX_COLS)] for _ in range(MAX_ROWS)]
    curr = [[False for _ in range(MAX_COLS)] for _ in range(MAX_ROWS)]
    prev[start[0]][start[1]] = True

    for _ in range(steps):
        for i in range(MAX_ROWS):
            for j in range(MAX_COLS):
                has_neighbour = False
                for [dx, dy] in DIRS:
                    tx, ty = (i + dx) % MAX_COLS, (j + dy) % MAX_ROWS
                    if map[i][j] != "#" and map[tx][ty] != "#" and prev[tx][ty]:
                        has_neighbour = True
                        break
                curr[i][j] = has_neighbour
        prev = deepcopy(curr)

    return sum(sum(1 for i in j if i) for j in curr)


def walk_bfs(steps):
    distances = {start: 0}
    q = []
    q.append(start)

    for dist in range(1, steps + 1):
        q2 = []
        while len(q):
            x, y = q.pop(0)
            for dx, dy in DIRS:
                new_x, new_y = x + dx, y + dy
                mod_x, mod_y = new_x % MAX_COLS, new_y % MAX_ROWS
                if map[mod_x][mod_y] != "#" and (new_x, new_y) not in distances:
                    distances[(new_x, new_y)] = dist
                    q2.append((new_x, new_y))
        q = q2

    return len([i for i in distances.values() if i % 2 == steps % 2])


###############################################################################


# Got quadratic formula from reddit
def solve_p2():
    size = MAX_ROWS
    half = size // 2
    y = [walk_bfs(half + i * size) for i in range(3)]

    a = (y[2] - (2 * y[1]) + y[0]) // 2
    b = y[1] - y[0] - a
    c = y[0]

    x = (26501365 - half) // size

    return a * x**2 + b * x + c


###############################################################################

input_file = "test.txt" if "test" in sys.argv else "input.txt"
lines = open(input_file).read().splitlines()

map = [list(a) for a in lines]
MAX_ROWS = len(map)
MAX_COLS = len(map[0])

start = (0, 0)
for i in range(MAX_ROWS):
    for j in range(MAX_COLS):
        if map[i][j] == "S":
            start = (i, j)
            break


print(f"Answer for Part 1: {get_garden_plots(64)}")
print(f"Answer for Part 1 (BFS Solution): {walk_bfs(64)} ")
print(f"Answer for Part 2: {solve_p2()}")
