import math

# Bottom up dynamic programming Time : (v*e) in complete graph Time : O(v*e^2) --> O(v^3)
def bellmenFord(adj, s):
    n = len(adj)
    dist = [math.inf] * n
    dist[s] = 0
    isRelaxed = True
    for _ in range(n-1):
        if not isRelaxed:
            break
        isRelaxed = False
        for u in range(n):
            for v, cost in adj[u]:
                if dist[v] > dist[u] + cost:
                    dist[v] = dist[u] + cost
                    isRelaxed = True
    return dist

# A - 0, B - 1, C - 2, D - 3, E - 4, F - 5, G - 6, H - 7, I - 8
adj = [[] for _ in range(9)]
def addEdge(u: int, v: int, w: int):
    adj[u].append((v, w))
    adj[v].append((u, w))

addEdge(0, 1, 4)
addEdge(0, 7, 8)
addEdge(1, 2, 8)
addEdge(1, 7, 11)
addEdge(2, 3, 7)
addEdge(2, 8, 2)
addEdge(2, 5, 4)
addEdge(3, 4, 9)
addEdge(3, 5, 14)
addEdge(4, 5, 10)
addEdge(5, 6, 2)
addEdge(6, 7, 1)
addEdge(6, 8, 6)
addEdge(7, 8, 7)

print(bellmenFord(adj, 0))
# [0, 4, 12, 19, 21, 11, 9, 8, 14]