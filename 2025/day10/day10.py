import z3

###############################################################################


def solve(part2):
    res = 0

    for i in open("in.txt").read().splitlines():
        s = i.split()
        lights = [1 if j == "#" else 0 for j in s[0][1:-1]]
        buttons = [[int(k) for k in j[1:-1].split(",")] for j in s[1:-1]]
        joltage = [int(k) for k in s[-1][1:-1].split(",")]

        z = z3.Optimize()
        v = [z3.Int(f"x_{j}") for j in range(len(buttons))]

        for j in range(len(buttons)):
            z.add(v[j] >= 0)
        for j in range(len(lights)):
            zz = sum(v[k] for k, b in enumerate(buttons) if j in b)
            z.add(zz == joltage[j] if part2 else zz % 2 == lights[j])

        z.minimize(sum(v))
        assert z.check() == z3.sat

        m = z.model()
        for x in v:
            res += m[x].as_long()

    return res


###############################################################################

print(f"Answer for Part 1: {solve(False)}")
print(f"Answer for Part 2: {solve(True)}")
