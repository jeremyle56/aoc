import sys
from copy import deepcopy
import networkx as nx
import math

###############################################################################


def solve_p1():
    components_complete = deepcopy(components)
    for i in components:
        for j in components[i]:
            if j not in components_complete:
                components_complete[j] = [i]
            elif i not in components_complete[j]:
                components_complete[j].append(i)

    G = nx.Graph()
    G.add_nodes_from(components_complete.keys())

    for i in components_complete:
        for j in components_complete[i]:
            G.add_edge(i, j)

    G.remove_edges_from(nx.minimum_edge_cut(G))
    return math.prod([len(i) for i in nx.connected_components(G)])


###############################################################################

input_file = "test.txt" if "test" in sys.argv else "input.txt"
lines = open(input_file).read().splitlines()

lines = [i.split(": ") for i in lines]
components = dict((i[0], i[1].split()) for i in lines)

print(f"Answer for Part 1: {solve_p1()}")
