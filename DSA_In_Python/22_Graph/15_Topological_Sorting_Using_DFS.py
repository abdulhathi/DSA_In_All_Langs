def topoSortUsingDFS(adj):
    n = len(adj)
    visited = [False] * n
    st = []
    def dfs(adj, u):
        visited[u] = True
        for v in adj[u]:
            if visited[v]:
                continue
            dfs(adj, v)
        st.append(u)
    
    for s in range(n):
        if visited[s]:
            continue
        dfs(adj, s)
    
    return st[::-1]

adj = [[1],[3],[3,4],[4],[]]
print(topoSortUsingDFS(adj))