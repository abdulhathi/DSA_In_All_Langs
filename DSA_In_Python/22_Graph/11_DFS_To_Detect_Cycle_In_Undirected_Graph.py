# Time : O(v+e) Space : O(v)
def dfsToDetectCycleInUndirectedGraph(adj):
    n = len(adj)
    visited = [False] * n

    def dfs(adj, u, p):
        visited[u] = True
        for v in adj[u]:
            if visited[v] and v != p:
                return True
            if visited[v] and v == p:
                continue
            if dfs(adj, v, u):
                return True
        return False
    
    for s in range(n):
        if visited[s]:
            continue
        if dfs(adj, s, None):
            return True
    return False


adj = [[1],[0,2,3],[1,3],[1,2]]
print(dfsToDetectCycleInUndirectedGraph(adj))

adj = [[1],[2,4],[1,3],[2],[1]]
print(dfsToDetectCycleInUndirectedGraph(adj))