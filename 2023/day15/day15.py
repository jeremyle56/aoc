import sys


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
    boxes = {i: [] for i in range(256)}

    for s in lines:
        label = s.split("-")[0]
        if "=" not in label:
            hash_value = hash(label)
            boxes[hash_value] = [i for i in boxes[hash_value] if i[0] != label]
        else:
            label = s.split("=")[0]
            focal = int(s.split("=")[1])
            hash_value = hash(label)
            hasLabel = [i for i in boxes[hash_value] if i[0] == label]
            if hasLabel:
                for i in range(len(boxes[hash_value])):
                    if boxes[hash_value][i][0] == label:
                        boxes[hash_value][i] = (label, focal)
            else:
                boxes[hash_value].append((label, focal))

    res = 0
    for i, j in boxes.items():
        for k in range(len(j)):
            res += (i + 1) * (k + 1) * j[k][1]

    return res


###############################################################################

input_file = "test.txt" if "test" in sys.argv else "input.txt"
with open(input_file) as f:
    lines = f.read().strip().split(",")

print(f"Answer for Part 1: {solve_p1()}")
print(f"Answer for Part 2: {solve_p2()}")
