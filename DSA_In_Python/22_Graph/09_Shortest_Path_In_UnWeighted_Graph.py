from collections import deque

# Time : O(v+e) Space : O(v)
def shortestPathInUnWeightedGraph(adj, s):
    visited = [False] * len(adj)
    dist = [0] * len(adj)
    queue = deque([s])
    visited[s] = True
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if visited[v]:
                continue
            dist[v] = dist[u] + 1
            visited[v] = True
            queue.append(v)
    return dist

adj = [[1,2,3],[0,2,3],[0,1,3],[1,2]]
print(shortestPathInUnWeightedGraph(adj, 0))

adj = [[1,2,4],[0,3],[0,4,3],[1,2,5],[0,2,5],[3,4]]
print(shortestPathInUnWeightedGraph(adj, 0))