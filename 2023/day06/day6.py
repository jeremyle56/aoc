import collections, math, sys, re

# Brute Force Solution

###############################################################################


def solve_p1():
    time = [int(i) for i in times]
    distance = [int(i) for i in distances]

    res = 1

    for i in range(len(time)):
        min_hold_time = time[i]
        max_hold_time = 0
        for hold_time in range(1, time[i] - 1):
            if hold_time * (time[i] - hold_time) > distance[i]:
                min_hold_time = min(hold_time, min_hold_time)
                max_hold_time = max(hold_time, max_hold_time)
        res *= max_hold_time - min_hold_time + 1

    print(f"Answer for Part 1: {res}")


###############################################################################


def solve_p2():
    timeP2 = int("".join(times))
    distanceP2 = int("".join(distances))

    min_hold_time = timeP2
    max_hold_time = 0

    for hold_time in range(1, timeP2 - 1):
        if hold_time * (timeP2 - hold_time) > distanceP2:
            min_hold_time = min(hold_time, min_hold_time)
            max_hold_time = max(hold_time, max_hold_time)

    print(f"Answer for Part 2: {max_hold_time - min_hold_time + 1}")


###############################################################################


lines = open("input.txt").read().splitlines()
times = lines[0][11:].split()
distances = lines[1][11:].split()
solve_p1()
solve_p2()
