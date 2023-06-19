import heapq

# Time : O(m*n log(m))
def mergeKSortedArray(arr):
    k = len(arr)
    res, minHeap = [], []
    for r in range(k):
        heapq.heappush(minHeap, (arr[r][0], r, 0))

    while minHeap:
        val, r, c = heapq.heappop(minHeap)
        res.append(val)
        if c+1 < len(arr[r]):
            heapq.heappush(minHeap, (arr[r][c+1], r, c+1))

    # print(minHeap)
    return res

print(mergeKSortedArray([[10,20,30],[5,15],[1,8,11,18]]))

"""
    [10,20,30]
    [5,15]
    [1,8,11,18]
"""