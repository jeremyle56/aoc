import sys
import numpy as np


def get_max_size(s):
    return sum(int(i[1]) for i in plan if i[0] == s)


def mark_grid(grid, amount, x, y, dx, dy):
    for _ in range(amount):
        grid[x + dx][y + dy] = "#"
        x += dx
        y += dy
    return (x, y)


# https://stackoverflow.com/questions/41077185/fastest-way-to-shoelace-formula
def shoelace(x_y):
    x_y = np.array(x_y)
    x_y = x_y.reshape(-1, 2)

    x = x_y[:, 0]
    y = x_y[:, 1]

    s1 = np.sum(x * np.roll(y, -1))
    s2 = np.sum(y * np.roll(x, -1))

    return 0.5 * np.abs(s1 - s2)


###############################################################################


def solve_p1():
    grid = [["." for _ in range(max)] for _ in range(max)]
    grid[0][0] = "#"
    cur = (0, 0)
    pos = []
    pos.append(cur)

    for i in plan:
        match i[0]:
            case "U":
                cur = mark_grid(grid, i[1], cur[0], cur[1], -1, 0)
            case "D":
                cur = mark_grid(grid, i[1], cur[0], cur[1], 1, 0)
            case "L":
                cur = mark_grid(grid, i[1], cur[0], cur[1], 0, -1)
            case "R":
                cur = mark_grid(grid, i[1], cur[0], cur[1], 0, 1)
        pos.append(cur)

    # for i in grid:
    #     for j in i:
    #         print(j, end="")
    #     print()

    return shoelace(pos[:-1]) + sum(i[1] for i in plan) // 2 + 1


###############################################################################


def solve_p2():
    hex = [i[2].replace("#", "") for i in plan]
    hex = [[int(i[-1]), i[:5]] for i in hex]
    direction = ["R", "D", "L", "U"]
    p2 = [[direction[i[0]], int(i[1], 16)] for i in hex]
    cur = (0, 0)
    pos = [cur]

    for i in p2:
        match i[0]:
            case "U":
                cur = (cur[0] - i[1], cur[1])
            case "D":
                cur = (cur[0] + i[1], cur[1])
            case "L":
                cur = (cur[0], cur[1] - i[1])
            case "R":
                cur = (cur[0], cur[1] + i[1])
        pos.append(cur)

    return shoelace(pos[:-1]) + sum(i[1] for i in p2) // 2 + 1


###############################################################################

input_file = "test.txt" if "test" in sys.argv else "input.txt"
lines = open(input_file).read().splitlines()
temp = [i.replace("(", "").replace(")", "").split() for i in lines]
plan = [[x, int(y), z] for x, y, z in temp]

max = max(get_max_size("U"), get_max_size("D"), get_max_size("L"), get_max_size("R"))

print(f"Answer for Part 1: {solve_p1()}")
print(f"Answer for Part 2: {solve_p2()}")
