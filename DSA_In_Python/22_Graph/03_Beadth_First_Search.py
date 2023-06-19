from collections import deque

# Time : O(v+e) Space : O(v)
def bfs(adj, s):
    visited = [False] * len(adj)
    queue = deque([s])
    visited[s] = True
    res = []
    while queue:
        u = queue.popleft()
        res.append(u)
        for v in adj[u]:
            if visited[v]:
                continue
            queue.append(v)
            visited[v] = True
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
print(bfs(adj, 0))