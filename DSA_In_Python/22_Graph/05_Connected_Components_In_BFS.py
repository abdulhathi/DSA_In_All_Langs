from collections import deque

def connectedCompsInBFS(adj):
    visited = [False] * len(adj)
    def bfs(adj, s):
        queue = deque([s])
        visited[s] = True
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if visited[v]:
                    continue
                queue.append(v)
                visited[v] = True
    
    count = 0
    for i in range(len(adj)):
        if visited[i]:
            continue
        bfs(adj, i)
        count += 1
    return count

adj = [[1,2],[0,2],[0,1],[4],[3],[6,7],[5],[5]]
print(connectedCompsInBFS(adj))