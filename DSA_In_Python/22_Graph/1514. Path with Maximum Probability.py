import heapq

class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:
        adj = [[] for _ in range(n)]
        for i in range(len(edges)):
            u,v = edges[i]
            c = succProb[i]
            adj[u].append((v, c))
            adj[v].append((u, c))

        dist = [0.0] * n
        visited = [False] * n
        maxHeap = [(-1.0, start)]

        while maxHeap:
            w, u = heapq.heappop(maxHeap)
            if visited[u]:
                continue
            visited[u] = True
            for v, c in adj[u]:
                if not visited[v] and (c * (-w)) > dist[v]:
                    dist[v] = c * (-w)
                    heapq.heappush(maxHeap, ((c*w), v))
        print(dist)
        return dist[end]

# print(Solution().maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2],0,2))
print(Solution().maxProbability(5, 
                                [[2,3],[1,2],[3,4],[1,3],[1,4],[0,1],[2,4],[0,4],[0,2]], 
                                [0.06,0.26,0.49,0.25,0.2,0.64,0.23,0.21,0.77],0,3))
"""
    heap = [(-1.0, 0)]                  visited = [  0,   1,   2]
    heap = [(-0.5, 1), (-0.2, 2)]       dist    = [0.0, 0.5, 0.25]
    heap = [(-0.25, 2), (-0.2, 2)]
"""