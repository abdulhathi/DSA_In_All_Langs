
# Time : O(v+e) space : O(v)
def dfs(adj, s):
    visited = [False] * len(adj)
    res = []
    def dfsRecursive(adj, u):
        visited[u] = True
        res.append(u)
        for v in adj[u]:
            if visited[v]:
                continue
            dfsRecursive(adj, v)
    
    dfsRecursive(adj, s)
    return res


"""         (1)--------(3)
          /  |        / |
        /    |      /   |
    (0)      |    /     |
        \    |  /       |
         \   |/         |
           (2)--------(4)    
"""
adj = [[1,2],[0,2,3],[0,1,3,4],[1,2,4],[2,3]]
print(dfs(adj, 0))