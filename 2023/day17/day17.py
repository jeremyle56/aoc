import math
import sys
import heapq


def isValid(row, col, dir, new_dir, num_dir, new_num_dir, part2):
    # part 1: can only move up to 3 times in one director
    p1_move = new_num_dir <= 3

    # part 2: can move at most 10 times, minimum 4 times
    # or cases are: building up to 4, already above minimum, at start
    p2_move = new_num_dir <= 10 and (new_dir == dir or num_dir >= 4 or dir == -1)
    move_constraint = p2_move if part2 else p1_move

    return (
        0 <= row < NUM_ROWS
        and 0 <= col < NUM_COLS
        and (new_dir + 2) % 4 != dir
        and move_constraint
    )


###############################################################################


def solve(part2):
    # row, col, dist, direction, num moves in direction
    q = [(0, 0, 0, -1, -1)]
    dist = {}

    while len(q):
        distance, row, col, dir, num_dir = heapq.heappop(q)
        if (row, col, dir, num_dir) in dist:
            continue

        dist[(row, col, dir, num_dir)] = distance
        # up, right, down, left
        for i, [dx, dy] in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
            new_row = row + dx
            new_col = col + dy
            new_dir = i
            new_num_dir = (num_dir + 1) if dir == new_dir else 1

            if isValid(new_row, new_col, dir, new_dir, num_dir, new_num_dir, part2):
                heapq.heappush(
                    q,
                    (
                        distance + map[new_row][new_col],
                        new_row,
                        new_col,
                        new_dir,
                        new_num_dir,
                    ),
                )

    res = math.inf

    for (row, col, _, _), d in dist.items():
        if row == NUM_ROWS - 1 and col == NUM_COLS - 1:
            res = min(res, d)

    return res


###############################################################################

input_file = "test.txt" if "test" in sys.argv else "input.txt"
lines = open(input_file).read().splitlines()
map = [[int(i) for i in j] for j in lines]

NUM_ROWS = len(map)
NUM_COLS = len(map[0])

print(f"Answer for Part 1: {solve(False)}")
print(f"Answer for Part 2: {solve(True)}")
