import sys

dirs = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

###############################################################################


def solve_p1(start_pos, start_dir):
    layout = [list(i) for i in lines]
    marked = set()

    # starts off the grid, i.e. start for p1 is [0, -1]
    stack = [(start_pos, dirs[start_dir])]

    while len(stack):
        start, dir = stack.pop()
        x, y = start
        dx, dy = dir

        if (x, y, dx, dy) in marked:
            continue
        marked.add((x, y, dx, dy))
        x += dx
        y += dy

        if x >= len(layout) or x < 0 or y >= len(layout[0]) or y < 0:
            continue

        if layout[x][y] == "/":
            stack.append(([x, y], [-dy, -dx]))
        elif layout[x][y] == "\\":
            stack.append(([x, y], [dy, dx]))
        elif layout[x][y] == "|" and dy != 0:
            stack.append(([x, y], dirs["up"]))
            stack.append(([x, y], dirs["down"]))
        elif layout[x][y] == "-" and dx != 0:
            stack.append(([x, y], dirs["left"]))
            stack.append(([x, y], dirs["right"]))
        else:
            stack.append(([x, y], [dx, dy]))

        # while True:
        #     if (
        #         x + dx >= len(layout)
        #         or x + dx < 0
        #         or y + dy >= len(layout[0])
        #         or y + dy < 0
        #         or (x + dx, y + dy, dx, dy) in marked
        #     ):
        #         break
        #     x += dx
        #     y += dy
        #     marked.add((x, y, dx, dy))
        #     if layout[x][y] == "/":
        #         temp_dy = dy
        #         dy = -dx
        #         dx = -temp_dy
        #     elif layout[x][y] == "\\":
        #         temp_dy = dy
        #         dy = dx
        #         dx = temp_dy
        #     elif layout[x][y] == "|" and (
        #         [dx, dy] == dirs["left"] or [dx, dy] == dirs["right"]
        #     ):
        #         stack.append(([x, y], dirs["up"]))
        #         stack.append(([x, y], dirs["down"]))
        #         break
        #     elif layout[x][y] == "-" and (
        #         [dx, dy] == dirs["up"] or [dx, dy] == dirs["down"]
        #     ):
        #         stack.append(([x, y], dirs["left"]))
        #         stack.append(([x, y], dirs["right"]))
        #         break

    # mapping = [["." for _ in j] for j in lines]
    # for x, y, _, _ in marked:
    #     mapping[x][y] = "#"
    # for i in mapping:
    #     for j in i:
    #         print(j, end="")
    #     print()

    return len({(x, y) for x, y, _, _ in marked}) - 1


###############################################################################


def solve_p2():
    res = 0

    for i in range(len(lines[0])):
        res = max(res, solve_p1([-1, i], "down"))
        res = max(res, solve_p1([len(lines), i], "up"))

    for i in range(len(lines)):
        res = max(res, solve_p1([i, -1], "right"))
        res = max(res, solve_p1([i, len(lines[0])], "left"))
    return res


###############################################################################

input_file = "test.txt" if "test" in sys.argv else "input.txt"
lines = open(input_file).read().splitlines()

print(f"Answer for Part 1: {solve_p1([0, -1], "right")}")
print(f"Answer for Part 2: {solve_p2()}")
