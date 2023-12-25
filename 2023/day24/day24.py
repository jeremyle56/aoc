import sys


def convert_to_int(l):
    return [int(x) for x in l]


def intersect_2d(a_pos, a_dir, b_pos, b_dir):
    a_pos = convert_to_int(a_pos)
    a_dir = convert_to_int(a_dir)
    b_pos = convert_to_int(b_pos)
    b_dir = convert_to_int(b_dir)

    x0a, y0a, _ = a_pos
    dxa, dya, _ = a_dir
    x0b, y0b, _ = b_pos
    dxb, dyb, _ = b_dir

    if (dxa * dyb - dxb * dya) == 0:
        return (-1, -1)

    t = (dyb * (x0b - x0a) - dxb * (y0b - y0a)) / (dxa * dyb - dxb * dya)
    t2 = min(t, (dya * (x0a - x0b) - dxa * (y0a - y0b)) / (dxb * dya - dxa * dyb))

    if t2 < 0:
        return (-1, -1)

    return (x0a + dxa * t, y0a + dya * t)


###############################################################################


def solve_p1():
    res = 0

    for i in range(len(hailstone_list)):
        a_pos = hailstone_list[i]
        a_dir = hailstone[a_pos]
        for j in range(i, len(hailstone_list)):
            b_pos = hailstone_list[j]
            b_dir = hailstone[b_pos]
            x_int, y_int = intersect_2d(a_pos, a_dir, b_pos, b_dir)
            if AREA_MIN <= x_int <= AREA_MAX and AREA_MIN <= y_int <= AREA_MAX:
                res += 1

    return res


###############################################################################


def solve_p2():
    res = 0
    return res


###############################################################################

input_file = "test.txt" if "test" in sys.argv else "input.txt"
AREA_MIN = 7 if "test" in sys.argv else 200000000000000
AREA_MAX = 27 if "test" in sys.argv else 400000000000000
lines = open(input_file).read().splitlines()

lines = [" ".join(i.split()) for i in lines]
lines = [i.split(" @ ") for i in lines]

hailstone_list = [tuple(i[0].split(", ")) for i in lines]
hailstone = dict((tuple(i[0].split(", ")), i[1].split(", ")) for i in lines)

print(f"Answer for Part 1: {solve_p1()}")
print(f"Answer for Part 2: {solve_p2()}")
