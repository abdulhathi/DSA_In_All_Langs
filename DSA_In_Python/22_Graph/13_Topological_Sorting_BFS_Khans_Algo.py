from collections import deque

# Time : O(v+e) Space : O(v)
def topologicalSorting(adj):
    n = len(adj)
    indegree = [0] * n
    for row in adj:
        for r in row:
            indegree[r] += 1
    
    queue = deque([u for u, count in enumerate(indegree) if count == 0])
    res = []

    count = 0
    while queue:
        u = queue.popleft()
        res.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
        count += 1

    return res, count

adj = [[2,3],[3,4],[3],[],[]]
print(topologicalSorting(adj))

adj = [[1,2],[3],[3],[4,5],[],[]]
print(topologicalSorting(adj))