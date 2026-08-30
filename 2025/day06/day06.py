import sys
import re

###############################################################################


def solve_p1():
    res = 0
    for i in range(len(operations)):
        temp = 0 if operations[i] == "+" else 1
        for j in numbers[i]:
            if operations[i] == "+":
                temp += j
            else:
                temp *= j
        res += temp

    return res


def solve_p2():
    new = []
    for i in range(len(lines[-1])):
        if lines[-1][i] == "+" or lines[-1][i] == "*":
            new.append(i)

    thing = []
    for i in range(len(new)):
        temp = []
        for j in range(len(lines) - 1):
            if i == len(new) - 1:
                temp.append(lines[j][new[i] :])
            else:
                temp.append(lines[j][new[i] : new[i + 1] - 1])
        thing.append(temp)

    res = 0
    for i in range(len(new)):
        temp = 0 if operations[i] == "+" else 1

        da_numbers = []
        for j in range(len(thing[i][0]) - 1, -1, -1):
            build = ""
            for k in thing[i]:
                if k[j] == " ":
                    continue
                build += k[j]
            da_numbers.append(int(build))

        print(da_numbers)
        for j in da_numbers:
            if operations[i] == "+":
                temp += j
            else:
                temp *= j

        res += temp

    return res


###############################################################################

lines = open("in.txt").read().splitlines()

numbers = [
    [int(j) for j in re.sub(r"\s+", " ", i).strip().split(" ")] for i in lines[:-1]
]
numbers = list(map(list, zip(*numbers)))

operations = re.sub(r"\s+", " ", lines[-1]).strip().split(" ")

print(f"Answer for Part 1: {solve_p1()}")
print(f"Answer for Part 2: {solve_p2()}")
