from collections import deque
import math

# Time : O(v+e) Space : O(v)
def shortestPathUsingTopologicalSorting(adj):
    n = len(adj)
    indegree = [0] * n
    res = [math.inf] * n
    for u in range(n):
        for v,_ in adj[u]:
            indegree[v] += 1

    for u, count in enumerate(indegree):
        if count == 0:
            res[u] = 0
            queue = deque([u])

    while queue:
        u = queue.popleft()
        for v,cost in adj[u]:
            indegree[v] -= 1
            res[v] = min(res[v], cost + res[u])
            if indegree[v] == 0:
                queue.append(v)
    
    return res

adj = [[(1,2),(4,1)],[(2,3)],[(3,6)],[],[(2,2),(5,4)],[(3,1)]]
print(shortestPathUsingTopologicalSorting(adj))