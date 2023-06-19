def dfsForConnectedComponents(adj):
    visited = [False] * len(adj)
    def dfs(adj, u):
        visited[u] = True
        for v in adj[u]:
            if visited[v]:
                continue
            dfs(adj, v)
    
    count = 0
    for s in range(len(adj)):
        if visited[s]:
            continue
        dfs(adj, s)
        count += 1
    return count

adj = [[1,2],[0,2],[0,1],[4],[3],[6,7],[5],[5]]
print(dfsForConnectedComponents(adj))