import sys

dirs = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}


# Finds the path for the ray of light
# start_pos is off the grid, i.e. start of Part 1 is [0, -1]
def bfs(start_pos, start_dir):
    marked = set()
    queue = [(start_pos, dirs[start_dir])]

    while len(queue):
        start, dir = queue.pop()
        x, y = start
        dx, dy = dir

        if (x, y, dx, dy) in marked:
            continue
        marked.add((x, y, dx, dy))

        x += dx
        y += dy

        if not (0 <= x < len(layout) and 0 <= y < len(layout[0])):
            continue

        if layout[x][y] == "/":
            queue.append(([x, y], [-dy, -dx]))
        elif layout[x][y] == "\\":
            queue.append(([x, y], [dy, dx]))
        elif layout[x][y] == "|" and dy != 0:
            queue.append(([x, y], dirs["up"]))
            queue.append(([x, y], dirs["down"]))
        elif layout[x][y] == "-" and dx != 0:
            queue.append(([x, y], dirs["left"]))
            queue.append(([x, y], dirs["right"]))
        else:
            queue.append(([x, y], [dx, dy]))

    return len({(x, y) for x, y, _, _ in marked}) - 1


###############################################################################


def solve_p1():
    return bfs([0, -1], "right")


###############################################################################


def solve_p2():
    res = 0

    for i in range(len(layout[0])):
        res = max(res, bfs([-1, i], "down"))
        res = max(res, bfs([len(layout), i], "up"))

    for i in range(len(layout)):
        res = max(res, bfs([i, -1], "right"))
        res = max(res, bfs([i, len(layout[0])], "left"))

    return res


###############################################################################

input_file = "test.txt" if "test" in sys.argv else "input.txt"
lines = open(input_file).read().splitlines()
layout = [list(i) for i in lines]

print(f"Answer for Part 1: {solve_p1()}")
print(f"Answer for Part 2: {solve_p2()}")
