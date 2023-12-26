import re
import sys
from z3 import Solver, Ints, Reals


def convert_to_int(listA):
    return [int(x) for x in listA]


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


# Tried other solutions but they didn't seem to terminate.
# This solution is copied from:
# https://www.reddit.com/r/adventofcode/comments/18pnycy/comment/kev3buh/?utm_source=share&utm_medium=web2x&context=3
def solve_p2():
    """
    Solve for 9 variables:

    three points in times: t1,t2,t3
    stone starting location: a,b,c
    stone starting speed: u,v,w

    stone:  S(t) = (a,b,c) + (u,v,w)*t
    hail 0: H0(t) = A0 + t*V0
    hail 1: H1(t) = A1 + t*V1
    hail 2: H2(t) = A2 + t*V2

    The stone trajectory intersects the three hails at three different times:
    S(t1) = H0(t1)
    S(t2) = H1(t2)
    S(t3) = H2(t3)

    Each of these gives rise to three equations (in the x, y, and z axes),
    giving the total of nine below.
    """

    with open(input_file) as f:
        new_lines = f.read().strip().split("\n")
    values = [list(map(int, re.findall(r"-?\d+", x))) for x in new_lines]
    three = values[:3]

    t1, t2, t3, a, b, c, u, v, w = Reals("t1 t2 t3 a b c u v w")
    A0x, A0y, A0z, V0x, V0y, V0z = three[0]
    A1x, A1y, A1z, V1x, V1y, V1z = three[1]
    A2x, A2y, A2z, V2x, V2y, V2z = three[2]
    eqs = [
        a + t1 * u == A0x + t1 * V0x,
        b + t1 * v == A0y + t1 * V0y,
        c + t1 * w == A0z + t1 * V0z,
        a + t2 * u == A1x + t2 * V1x,
        b + t2 * v == A1y + t2 * V1y,
        c + t2 * w == A1z + t2 * V1z,
        a + t3 * u == A2x + t3 * V2x,
        b + t3 * v == A2y + t3 * V2y,
        c + t3 * w == A2z + t3 * V2z,
    ]

    s = Solver()
    s.add(*eqs)
    s.check()
    res = s.model()
    return sum([res[x].as_long() for x in [a, b, c]])


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
