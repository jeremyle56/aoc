from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)


def get_neighbours(graph, x, y):
    neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    if graph[x][y] == ">":
        neighbours = [(x, y + 1)]
    elif graph[x][y] == "v":
        neighbours = [(x + 1, y)]
    elif graph[x][y] == "<":
        neighbours = [(x, y - 1)]
    elif graph[x][y] == "^":
        neighbours = [(x - 1, y)]

    return [(nx, ny) for nx, ny in neighbours if graph[nx][ny] != "#"]


def dfs(graph, x, y, visited):
    if (x, y) == end:
        return len(visited)

    neighbours = get_neighbours(graph, x, y)

    res = 0
    for n in neighbours:
        a, b = n
        if n in visited:
            continue

        visited.add(n)
        val = dfs(graph, a, b, visited)
        res = max(res, val)
        visited.remove(n)

    return res


###############################################################################


def solve_p1():
    return dfs(trail, start[0], start[1], set())


###############################################################################


# Help from: https://github.com/mgtezak/Advent_of_Code/blob/master/2023/Day_23.py
def solve_p2():
    new_trail = [[("#" if i == "#" else ".") for i in j] for j in trail]

    graph = defaultdict(list)
    q = [(start, start, {start})]

    while len(q):
        curr, prev, visited = q.pop(0)
        if curr == end:
            final_node = prev
            final_steps = len(visited) - 1
            continue

        x, y = curr
        neighbours = [i for i in get_neighbours(new_trail, x, y) if i not in visited]

        if len(neighbours) == 1:
            next = neighbours.pop()
            q.append((next, prev, visited | {next}))
        elif len(neighbours) > 1:
            steps = len(visited) - 1
            if (curr, steps) in graph[prev]:
                continue
            graph[prev].append((curr, steps))
            graph[curr].append((prev, steps))
            while neighbours:
                next = neighbours.pop(0)
                q.append((next, curr, {curr, next}))

    max_steps = 0
    queue = [(start, 0, {start})]
    while queue:
        curr, steps, visited = queue.pop()
        if curr == final_node:
            max_steps = max(steps, max_steps)
            continue
        for nxt, distance in graph[curr]:
            if nxt not in visited:
                queue.append((nxt, steps + distance, visited | {nxt}))

    return max_steps + final_steps


###############################################################################

input_file = "test.txt" if "test" in sys.argv else "input.txt"
lines = open(input_file).read().splitlines()

trail = [list(a) for a in lines]
MAX_ROW = len(trail)
MAX_COL = len(trail[0])

start = (0, 1)
end = (MAX_ROW - 1, MAX_COL - 2)

print(f"Answer for Part 1: {solve_p1()}")
print(f"Answer for Part 2: {solve_p2()}")
