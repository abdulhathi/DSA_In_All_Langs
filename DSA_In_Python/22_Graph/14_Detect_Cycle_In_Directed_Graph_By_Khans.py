from collections import deque

# Time : O(v+e)
def detectCycleUsingKhans(adj):
    n = len(adj)
    indegree = [0] * n
    for adjRow in adj:
        for v in adjRow:
            indegree[v] += 1
    
    queue = deque([u for u, count in enumerate(indegree) if count == 0])

    count = 0
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
        count += 1
    
    return count != n

adj = [[1],[],[1,3],[4],[5],[3]]
print(detectCycleUsingKhans(adj))

adj = [[1],[],[1,3],[4],[5],[]]
print(detectCycleUsingKhans(adj))