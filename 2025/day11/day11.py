from collections import defaultdict
from functools import cache

###############################################################################


def solve_p1():
    visited = defaultdict(bool)

    def dfs(node):
        if visited[node]:
            return 0
        if node == "out":
            return 1

        visited[node] = True
        a = sum([dfs(i) for i in adj[node]])
        visited[node] = False
        return a

    return dfs("you")


def solve_p2():
    @cache
    def dfs(node, fft, dac):
        if node == "out":
            return fft and dac

        return sum(
            [dfs(i, fft or (node == "fft"), dac or (node == "dac")) for i in adj[node]]
        )

    return dfs("svr", False, False)


###############################################################################

adj = {s[:-1]: set(v) for s, *v in map(str.split, open("in.txt"))}

print(f"Answer for Part 1: {solve_p1()}")
print(f"Answer for Part 2: {solve_p2()}")
