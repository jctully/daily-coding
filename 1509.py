'''
A graph is minimally-connected if it is connected and there is no edge that can be removed while still leaving the graph connected. For example, any binary tree is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected. You can choose to represent the graph as either an adjacency matrix or adjacency list.
'''
from collections import defaultdict

# by detecting cycles in an undirected graph. perform DFS and check if node has been seen, removing parent connection to avoid double counting
def is_min_connected(G: dict):
    seen = defaultdict(bool)
    S = [list(G.keys())[0]]

    while S:
        k = S.pop()
        if seen[k]:
            return False
        seen[k] = True
        for n in G[k]:
            G[n].remove(k)
        S += G[k]
    return True

# By definition of a tree. number of edges is 1 less than number of vertices
def is_min_connected(G: dict):
    V = len(G)
    E = 0

    for adj in G.values():
        E += len(adj)
    
    return E//2 == V-1


G_true = {
    'a': ['b', 'c'],
    'b': ['a','d' ],
    'c': ['a', ],
    'd': ['b', ],
       }
G_false = {
    'a': ['b', 'c'],
    'b': ['a', 'd' ],
    'c': ['a', 'd' ],
    'd': ['b', 'c'],
       }

print(is_min_connected(G_false))
