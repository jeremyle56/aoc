import copy


def north_tilt(tilted):
    for i in range(len(tilted)):
        for j in range(len(tilted[0])):
            if tilted[i][j] == "O":
                for k in range(i, 0, -1):
                    if tilted[k - 1][j] == ".":
                        tilted[k][j] = "."
                        tilted[k - 1][j] = "O"
                    else:
                        break


def west_tilt(tilted):
    for j in range(len(tilted[0])):
        for i in range(len(tilted)):
            if tilted[i][j] == "O":
                for k in range(j, 0, -1):
                    if tilted[i][k - 1] == ".":
                        tilted[i][k] = "."
                        tilted[i][k - 1] = "O"
                    else:
                        break


def south_tilt(tilted):
    for i in range(len(tilted) - 1, -1, -1):
        for j in range(len(tilted[0])):
            if tilted[i][j] == "O":
                for k in range(i, len(tilted) - 1):
                    if tilted[k + 1][j] == ".":
                        tilted[k][j] = "."
                        tilted[k + 1][j] = "O"
                    else:
                        break


def east_tilt(tilted):
    for j in range(len(tilted[0]) - 1, -1, -1):
        for i in range(len(tilted)):
            if tilted[i][j] == "O":
                for k in range(j, len(tilted[0]) - 1):
                    if tilted[i][k + 1] == ".":
                        tilted[i][k] = "."
                        tilted[i][k + 1] = "O"
                    else:
                        break


def calc_load(tilted):
    res = 0
    for i in range(len(tilted)):
        for j in tilted[i]:
            if j == "O":
                res += len(tilted) - i
    return res


###############################################################################


def solve_p1():
    tilted = copy.deepcopy(map)
    north_tilt(tilted)

    print(f"Answer for Part 1: {calc_load(tilted)}")


###############################################################################


def solve_p2():
    tilted = copy.deepcopy(map)

    # Problem required 1000000000 cycles but
    # after a point they are cyclic so no point, so use smaller number
    for _ in range(1000):
        north_tilt(tilted)
        west_tilt(tilted)
        south_tilt(tilted)
        east_tilt(tilted)

    print(f"Answer for Part 2: {calc_load(tilted)}")


###############################################################################


lines = open("input.txt").read().splitlines()
map = [list(i) for i in lines]

solve_p1()
solve_p2()
