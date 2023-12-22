import sys
from copy import deepcopy


def drop_bricks(bricks):
    bricks_sorted = sorted(bricks, key=lambda bks: min(b[2] for b in bks))

    stable = set()
    final_state = []
    num_fell = 0

    for brick in bricks_sorted:
        moved = False
        while True:
            next = set()
            for x, y, z in brick:
                next.add((x, y, z - 1))

            if all((b[2] != 0 and (b not in stable)) for b in next):
                brick = next
                moved = True
            else:
                break

        for cube in brick:
            stable.add(cube)
        final_state.append(brick)
        num_fell += 1 if moved else 0

    return final_state, num_fell


###############################################################################


def solve():
    p1 = 0
    p2 = 0

    for i in range(len(bricks)):
        remove_brick = deepcopy(bricks)
        remove_brick.pop(i)
        _, num_fell = drop_bricks(remove_brick)
        p1 += 1 if num_fell == 0 else 0
        p2 += num_fell

    return p1, p2


###############################################################################

input_file = "test.txt" if "test" in sys.argv else "input.txt"
lines = open(input_file).read().splitlines()

bricks = []

for line in lines:
    start, end = line.split("~")
    start = tuple(int(n) for n in start.split(","))
    end = tuple(int(n) for n in end.split(","))

    cubes = set([start, end])
    for i in range(2):
        if start[i] != end[i]:
            for j in range(min(start[i], end[i]) + 1, max(start[i], end[i])):
                to_add = list(start)
                to_add[i] = j
                cubes.add(tuple(to_add))

    bricks.append(cubes)

bricks, _ = drop_bricks(bricks)
p1, p2 = solve()

print(f"Answer for Part 1: {p1}")
print(f"Answer for Part 2: {p2}")
