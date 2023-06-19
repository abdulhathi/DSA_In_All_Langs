from collections import deque

def bfsOfDisconnectedGraph(adj):
    visited = [False] * len(adj)
    res = []
    def bfs(adj, s):
        queue = deque([s])
        visited[s] = True
        while queue:
            u = queue.popleft()
            res.append(u)
            for v in adj[u]:
                if visited[v]:
                    continue
                queue.append(v)
                visited[v] = True
    
    for i in range(len(adj)):
        if visited[i]:
            continue
        bfs(adj, i)
    return res

adj = [[1,2],[0,3],[0,3],[1,2],[5,6],[4,6],[5,4]]
print(bfsOfDisconnectedGraph(adj))

