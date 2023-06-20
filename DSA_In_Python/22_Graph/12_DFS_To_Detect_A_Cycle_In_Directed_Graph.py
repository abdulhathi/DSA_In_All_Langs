# Time : O(v+e) Space : O(v)
def dfsToDetectCycleInDirectedGraph(adj):
    n = len(adj)
    visited = [False] * n
    recSt = [False] * n

    def dfs(adj, u):
        visited[u] = True
        recSt[u] = True
        for v in adj[u]:
            if recSt[v]:
                return True
            if visited[v]:
                continue
            if dfs(adj, v):
                return True
        recSt[u] = False
        return False
    
    for s in range(n):
        if visited[s]:
            continue
        if dfs(adj, s):
            return True
    return False

adj = [[1],[],[1,3],[4],[5],[3]]
print(dfsToDetectCycleInDirectedGraph(adj))

adj = [[1],[],[1,3],[4],[5],[]]
print(dfsToDetectCycleInDirectedGraph(adj))
