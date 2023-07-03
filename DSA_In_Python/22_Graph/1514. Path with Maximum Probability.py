# Python - Dijkstra's single source shortest path algo - Time : O(e + vlogv + elogv) Space : O(e+v)
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = [[] for _ in range(n)]
        for i in range(len(edges)):
            u,v = edges[i]
            c = succProb[i]
            adj[u].append((v, c))
            adj[v].append((u, c))

        dist = [0.0] * n
        visited = [False] * n
        maxHeap = [(-1.0, start)]
        dist[start] = [1.0]
        
        while maxHeap:
            w, u = heapq.heappop(maxHeap)
            if visited[u]:
                continue
            visited[u] = True
            
            for v, c in adj[u]:
                if not visited[v] and (c * (-w)) > dist[v]:
                    dist[v] = c * (-w)
                    heapq.heappush(maxHeap, ((c*w), v))
        return dist[end]


"""
    heap = [(-1.0, 0)]                  visited = [  0,   1,   2]
    heap = [(-0.5, 1), (-0.2, 2)]       dist    = [0.0, 0.5, 0.25]
    heap = [(-0.25, 2), (-0.2, 2)]
"""