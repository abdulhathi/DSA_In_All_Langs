import heapq, math

def primsMST(adj, s):
    n = len(adj)
    dist, visited = [math.inf] * n, [False] * n
    dist[s] = 0
    minHeap = [(0, s)]
    while minHeap:
        u, _ = heapq.heappop(minHeap)
        if visited[u]:
            continue
        visited[u] = True
        for v, c in adj[u]:
            if not visited[v] and c < dist[v]:
                dist[v] = c
                heapq.heappush(minHeap, (v, c))
    return dist


"""
                (1)
               / | 
              5  |  
            /    |
        (0)      10 
          \       |  
           8     |
            \   |
              (2)
"""
print(primsMST([[(1,5),(2,8)],[(0,5),(2,10),(3,15)],[(0,8),(1,10),(3,20)],[(1,15),(2,20)]], 0))

