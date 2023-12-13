def find_reflection(pattern, ignore=-1):
    for left in range(1, len(pattern[0]) + 1):
        right = len(pattern[0]) - left
        if left != ignore:
            if left > right and all(
                list(reversed(p[-right:])) == p[-(right * 2) : -right] for p in pattern
            ):
                return left
            elif all(list(reversed(p[:left])) == p[left : left * 2] for p in pattern):
                return left

    for top in range(1, len(pattern)):
        bottom = len(pattern) - top
        if 100 * top != ignore:
            if top > bottom:
                if all(pattern[top - x - 1] == pattern[top + x] for x in range(bottom)):
                    return 100 * top
            elif all(pattern[top - x - 1] == pattern[top + x] for x in range(top)):
                return 100 * top

    return -1


###############################################################################


def solve_p1():
    res = 0

    for i in patterns:
        res += find_reflection(i)

    print(f"Answer for Part 1: {res}")


###############################################################################


def solve_p2():
    res = 0

    for i in patterns:
        ignore = find_reflection(i)
        done = False
        for j in range(len(i)):
            for k in range(len(i[0])):
                i[j][k] = "#" if i[j][k] == "." else "."
                val = find_reflection(i, ignore=ignore)
                i[j][k] = "#" if i[j][k] == "." else "."
                if val > 0 and val != ignore:
                    res += val
                    done = True
                    break
            if done:
                break

    print(f"Answer for Part 2: {res}")


###############################################################################


lines = open("input.txt").read().splitlines()
patterns = []
i = 0
while i < len(lines):
    temp = []
    while i < len(lines) and lines[i] != "":
        temp2 = []
        for j in range(len(lines[i])):
            temp2.append(lines[i][j])
        temp.append(temp2)
        i += 1
    patterns.append(temp)
    i += 1

solve_p1()
solve_p2()
