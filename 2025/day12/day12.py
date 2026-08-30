###############################################################################


def solve_p1():
    res = 0

    for i in regions:
        temp = 0
        for j in range(2, len(regions[0])):
            temp += ss[j - 2] * i[j]
        if i[0] * i[1] >= temp:
            res += 1

    return res


###############################################################################

lines = open("in.txt").read().split("\n\n")

shapes = [i.split()[1:] for i in lines[:-1]]
ss = [sum(sum(1 if j == "#" else 0 for j in i) for i in k) for k in shapes]
regionsTemp = lines[-1].strip().split("\n")

regions = []
for i in regionsTemp:
    s = i.split()
    x = int(s[0].split("x")[0])
    y = int(s[0].split("x")[1][:-1])
    rest = [int(i) for i in s[1:]]
    regions.append([x, y, *rest])

print(f"Answer for Part 1: {solve_p1()}")
