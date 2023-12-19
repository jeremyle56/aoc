import sys
from copy import deepcopy


def calc_combinations(ranges):
    res = 1
    for low, high in ranges.values():
        res *= high - low + 1
    return res


def find_num_combinations(ranges, workflow):
    res = 0
    for rule in workflows[workflow]:
        rule = rule.split(":")
        if len(rule) == 1:
            if rule == ["A"]:
                res += calc_combinations(ranges)
            elif rule != ["R"]:
                res += find_num_combinations(ranges, rule[0])
        else:
            condition, action = rule
            new_ranges = deepcopy(ranges)
            if ">" in condition:
                var, limit = condition.split(">")
                if new_ranges[var][1] > int(limit):
                    new_ranges[var][0] = max(new_ranges[var][0], int(limit) + 1)
                    if action == "A":
                        res += calc_combinations(new_ranges)
                    elif action != "R":
                        res += find_num_combinations(new_ranges, action)
                    ranges[var][1] = min(ranges[var][1], int(limit))
            else:
                var, limit = condition.split("<")
                if new_ranges[var][0] < int(limit):
                    new_ranges[var][1] = min(new_ranges[var][1], int(limit) - 1)
                    if action == "A":
                        res += calc_combinations(new_ranges)
                    elif action != "R":
                        res += find_num_combinations(new_ranges, action)
                    ranges[var][0] = max(ranges[var][0], int(limit))

    return res


###############################################################################


def solve_p1():
    res = 0
    for part in parts:
        part = part.split(",")
        x, m, a, s = [int(i[2:]) for i in part]

        rules = workflows["in"]
        while True:
            resolved = False
            for i in rules:
                i = i.split(":")
                condition = True if len(i) == 1 else eval(i[0])
                action = i[0] if len(i) == 1 else i[1]

                if condition:
                    if action == "A":
                        res += x + m + a + s
                        resolved = True
                    elif action == "R":
                        resolved = True
                    else:
                        rules = workflows[action]
                    break

            if resolved:
                break

    return res


###############################################################################


# Needed help from https://github.com/knosmos/advent-2023/blob/main/19/19b.py solution
def solve_p2():
    ranges = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}
    return find_num_combinations(ranges, "in")


###############################################################################

input_file = "test.txt" if "test" in sys.argv else "input.txt"
lines = open(input_file).read().split("\n\n")

workflows = lines[0].split()
parts = lines[1].replace("{", "").replace("}", "").split()

workflows = [[j for j in i.replace("}", "").split("{")] for i in workflows]
workflows = [[i, j.split(",")] for i, j in workflows]
workflows = dict((i[0], i[1]) for i in workflows)

print(f"Answer for Part 1: {solve_p1()}")
print(f"Answer for Part 2: {solve_p2()}")
