from collections import deque

# Time : O(v+e) Space : O(v)
def detectCycleInUnDirectedGraph(adj):
    n = len(adj)
    visited = [False] * n
    def bfs(adj, s):
        queue = deque([(s, None)])
        visited[s] = True
        while queue:
            u, p = queue.popleft()
            for v in adj[u]:
                if visited[v] and v != p:
                    return True
                if visited[v] and v == p:
                    continue
                queue.append((v, u))
                visited[v] = True
        return False
    
    for s in range(n):
        if visited[s]:
            continue
        if bfs(adj, s):
            return True
    return False

adj = [[1],[0,2,3],[1,3],[1,2]]
print(detectCycleInUnDirectedGraph(adj))

adj = [[1],[2,4],[1,3],[2],[1]]
print(detectCycleInUnDirectedGraph(adj))