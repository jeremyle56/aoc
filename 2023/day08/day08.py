import collections, math, sys, re


def num_steps(start, goal):
    res = 0

    while not start.endswith(goal):
        i = instructions[res % len(instructions)]
        start = network[start][0] if i == "L" else network[start][1]
        res += 1

    return res


###############################################################################


def solve_p1():
    print(f"Answer for Part 1: {num_steps('AAA', 'ZZZ')}")


###############################################################################
# Note: First attempt was brute force, takes too long


def solve_p2():
    start = [i for i in network.keys() if i.endswith("A")]
    values = [num_steps(i, "Z") for i in start]

    print(f"Answer for Part 2: {math.lcm(*values)}")


###############################################################################


lines = open("input.txt").read().splitlines()

instructions = lines[0]
network = {i[0]: [i[2][1:-1], i[3][:-1]] for i in [j.split() for j in lines[2:]]}

solve_p1()
solve_p2()
