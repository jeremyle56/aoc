import re, sys


def hash(s):
    res = 0
    for c in s:
        res += ord(c)
        res *= 17
        res %= 256
    return res


###############################################################################


def solve_p1():
    return sum(hash(s) for s in lines)


###############################################################################


def solve_p2():
    boxes = {i: {} for i in range(256)}

    for s in lines:
        label, focal = re.findall(r"([^=|-]*)(.*)", s)[0]
        box_num = hash(label)
        if "=" in s:
            boxes[box_num][label] = int(focal[1:])
        else:
            boxes[box_num].pop(label, "python werid")

    res = 0
    for i, box in boxes.items():
        for j, k in enumerate(box.values()):
            res += (i + 1) * (j + 1) * k

    return res


###############################################################################

input_file = "test.txt" if "test" in sys.argv else "input.txt"
with open(input_file) as f:
    lines = f.read().strip().split(",")

print(f"Answer for Part 1: {solve_p1()}")
print(f"Answer for Part 2: {solve_p2()}")
