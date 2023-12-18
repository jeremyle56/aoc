import sys

dirs = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
directions = ["R", "D", "L", "U"]

###############################################################################


def solve(part2):
    cur = (0, 0)
    points = [cur]
    perim = 0

    for i in hex if part2 else plan:
        diff_x, diff_y = dirs[i[0]]
        perim += i[1]
        cur = (cur[0] + diff_x * i[1], cur[1] + diff_y * i[1])
        points.append(cur)

    area = 0
    for i in range(len(points) - 1):
        area += (points[i][0] * points[i + 1][1]) - (points[i + 1][0] * points[i][1])

    return perim // 2 + abs(area) // 2 + 1


###############################################################################

input_file = "test.txt" if "test" in sys.argv else "input.txt"
lines = open(input_file).read().splitlines()
temp = [i.split() for i in lines]
plan = [[x, int(y)] for x, y, _ in temp]

temp1 = [i[2][2:-1] for i in temp]
hex = [[directions[int(i[-1])], int(i[:5], 16)] for i in temp1]


print(f"Answer for Part 1: {solve(False)}")
print(f"Answer for Part 2: {solve(True)}")
