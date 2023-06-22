from collections import deque

# Time O(v+e) Space : O(v+e)
def kosarajusStonglyConnComponents(adj):
    n = len(adj)
    visited = [False] * n
    st = []
    def dfs(u):
        visited[u] = True
        for v in adj[u]:
            if visited[v]:
                continue
            dfs(v)
        st.append(u)

    for u in range(n):
        if visited[u]:
            continue
        dfs(u)
    
    revAdj = [[] for _ in range(n)]
    visited = [False] * n

    for u in range(n):
        for v in adj[u]:
            revAdj[v].append(u)

    def bfsForRevGraph(revAdj, u):
        res = []
        queue = deque([u])
        visited[u] = True
        while queue:
            u = queue.popleft()
            res.append(u)
            for v in revAdj[u]:
                if visited[v]:
                    continue
                queue.append(v)
                visited[v] = True
        return res
    
    res = []
    while st:
        if visited[st[-1]]:
            st.pop()
            continue
        res.append(bfsForRevGraph(revAdj, st.pop()))
    return res

adj = [[1],[2,3],[0],[4],[]]
print(kosarajusStonglyConnComponents(adj))