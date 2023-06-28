import heapq

def kruskalsMST(adj):
    n = len(adj)
    parent = [i for i in range(n)]
    rank = [0] * n
    minHeap = []
    dist = [0] * n

    def find(u):
        if parent[u] == u:
            return parent[u]
        parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        pU, pV = find(u), find(v)
        if pU == pV:
            return
        if rank[pU] > rank[pV]:
            parent[pV] = pU
        elif rank[pV] > rank[pU]:
            parent[pU] = pV
        else:
            parent[pV] = pU
            rank[pU] += 1

    for u in range(n):
        for v, c in adj[u]:
            heapq.heappush(minHeap, (c, u, v))

    while minHeap:
        c, u, v = heapq.heappop(minHeap)
        if find(u) == find(v):
            continue
        union(u,v)
        dist[v] = c

    return dist


print(kruskalsMST([[(1,5),(2,8)],[(0,5),(2,10),(3,15)],[(0,8),(1,10),(3,20)],[(1,15),(2,20)]]))


print(max(0.25,0.2))