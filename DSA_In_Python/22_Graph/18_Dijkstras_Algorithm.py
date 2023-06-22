import heapq, math

# Time : O(vlogv + elogv) Space : O(v)
def dijkstrasAlgoSingleSourceShortestPath(adj, s):
    n = len(adj)
    dist = [math.inf] * n
    visited = [False] * n
    minHeap = [(0, s)]
    dist[s] = 0 
    while minHeap:
        cost, u = heapq.heappop(minHeap)
        if visited[u]:
            continue
        visited[u] = True
        for v, c in adj[u]:
            if not visited[v] and cost + c < dist[v]:
                dist[v] = cost+c
                heapq.heappush(minHeap, (cost+c, v))
    return dist

# A - 0, B - 1, C - 2, D - 3, E - 4, F - 5, G - 6, H - 7, I - 8
adj = [[] for _ in range(9)]
 
def addEdge(u: int, v: int, w: int):
    adj[u].append((v, w))
    adj[v].append((u, w))

addEdge(0, 1, 4)
addEdge(0, 7, 8)
addEdge(1, 2, 8)
addEdge(1, 7, 11)
addEdge(2, 3, 7)
addEdge(2, 8, 2)
addEdge(2, 5, 4)
addEdge(3, 4, 9)
addEdge(3, 5, 14)
addEdge(4, 5, 10)
addEdge(5, 6, 2)
addEdge(6, 7, 1)
addEdge(6, 8, 6)
addEdge(7, 8, 7)

# print(adj)

print(dijkstrasAlgoSingleSourceShortestPath(adj, 0))