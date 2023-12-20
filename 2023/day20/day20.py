from collections import defaultdict
from math import lcm
from sys import argv

###############################################################################


def solve_p1():
    num_low = 0
    num_high = 0

    # Off and low puluse is False
    states = {i[1:]: False for i in configuration}
    conjugate_memory = defaultdict(dict)

    for a, b in configuration.items():
        for c in b:
            if "&" + c in configuration.keys():
                conjugate_memory[c][a[1:]] = False

    for _ in range(1000):
        queue = [("broadcaster", False, "button")]
        while len(queue):
            dest, pulse, src = queue.pop(0)

            if pulse:
                num_high += 1
            else:
                num_low += 1

            if dest == "broadcaster":
                for i in configuration[dest]:
                    queue.append((i, pulse, dest))
            elif "%" + dest in configuration:
                if not pulse:
                    states[dest] = not states[dest]
                    for i in configuration["%" + dest]:
                        queue.append((i, states[dest], dest))
            elif "&" + dest in configuration:
                conjugate_memory[dest][src] = pulse
                pulse_send = not all(v for v in conjugate_memory[dest].values())
                for i in configuration["&" + dest]:
                    queue.append((i, pulse_send, dest))
    return num_low * num_high


###############################################################################


def solve_p2():
    rx_parent = ""
    for i, j in configuration.items():
        if "rx" in j:
            rx_parent = i[1:]
            break

    ancestors = set()
    for i, j in configuration.items():
        if rx_parent in j:
            ancestors.add(i[1:])

    # Off and low puluse is False
    states = {i[1:]: False for i in configuration}
    conjugate_memory = defaultdict(dict)

    for a, b in configuration.items():
        for c in b:
            if "&" + c in configuration.keys():
                conjugate_memory[c][a[1:]] = False

    res = []
    done_count = 0
    for r in range(1, 1000000000000000000000000):
        queue = [("broadcaster", False, "button")]
        while len(queue):
            dest, pulse, src = queue.pop(0)

            if not pulse and dest in ancestors:
                res.append(r)
                done_count += 1

            if dest == "broadcaster":
                for i in configuration[dest]:
                    queue.append((i, pulse, dest))
            elif "%" + dest in configuration:
                if not pulse:
                    states[dest] = not states[dest]
                    for i in configuration["%" + dest]:
                        queue.append((i, states[dest], dest))
            elif "&" + dest in configuration:
                conjugate_memory[dest][src] = pulse
                pulse_send = not all(v for v in conjugate_memory[dest].values())
                for i in configuration["&" + dest]:
                    queue.append((i, pulse_send, dest))

            if done_count >= len(ancestors):
                return lcm(*res)


###############################################################################

input_file = "input.txt"
if "test" in argv:
    input_file = "test.txt"
elif "test1" in argv:
    input_file = "test1.txt"
lines = open(input_file).read().splitlines()

configuration = {k: v.split(", ") for k, v in (i.split(" -> ") for i in lines)}

print(f"Answer for Part 1: {solve_p1()}")
print(f"Answer for Part 2: {solve_p2()}")
