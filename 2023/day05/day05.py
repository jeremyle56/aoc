import collections, math, sys, re

###############################################################################


def solve_p1():
    seedsMap = dict((i, i) for i in seeds)
    moved = dict((i, False) for i in seeds)

    for line in lines:
        if re.match(r"[^0-9 ]", line):
            moved = dict.fromkeys(moved, False)
            continue

        line = [int(i) for i in line.split()]
        [dest, src, length] = line

        for key, value in seedsMap.items():
            if value >= src and value < src + length and not moved[value]:
                seedsMap[key] = dest + (value - src)
                moved[dest + (value - src)] = True

    print(f"Answer for Part 1: {min(seedsMap.values())}")


###############################################################################


def solve_p2():
    res = []
    mappings = [[], [], [], [], [], [], []]

    count = -1
    for line in lines:
        if re.match(r"[^0-9 ]", line):
            count += 1
            continue
        line = line.split()
        mappings[count].append(tuple(int(i) for i in line))

    print(mappings)

    for i in range(0, len(seeds), 2):
        seed_start, seed_range, skip = seeds[i], seeds[i + 1], seeds[i + 1]
        cur_seed = seed_start
        while cur_seed <= seed_start + seed_range:
            r = cur_seed
            for translation in range(len(mappings)):
                for map in mappings[translation]:
                    if map[1] <= r < map[1] + map[2]:
                        skip = min(skip, map[1] + map[2] - r)
                        r += map[0] - map[1]
                        skip = 1 if skip <= 0 else skip
                        break
            res.append(r)
            cur_seed += skip
            skip = seed_range - cur_seed + seed_start

    print(f"Answer for Part 2: {min(res)}")


###############################################################################


lines = open("input.txt").read().splitlines()
seeds = [int(i) for i in lines[0].split(": ")[1].split()]

lines = [i for i in lines[1:] if i.strip()]

solve_p1()
solve_p2()
