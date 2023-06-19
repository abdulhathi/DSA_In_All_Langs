# Time : O(v+e)  Space : O(v)
def dfsForDisconnected(adj):
    visited = [False] * len(adj)
    res = []
    def dfs(adj, u):
        visited[u] = True
        res.append(u)
        for v in adj[u]:
            if visited[v]:
                continue
            dfs(adj, v)
    
    for s in range(len(adj)):
        if visited[s]:
            continue
        dfs(adj, s)
    return res

adj = [[1,2],[0,2],[0,1],[4],[3],[6,7],[5],[5]]
print(dfsForDisconnected(adj))