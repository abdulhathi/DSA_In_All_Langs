import heapq

# Time : O(n+k logk)
def sortKSortedArray(arr, k):
    pq, n = [], len(arr)
    # Time  : O(klogk)
    for i in range(k):
        heapq.heappush(pq, arr[i])
    # Time  : O(nlogk)
    for i in range(n):
        arr[i] = heapq.heappop(pq)
        if i+k < n:
            heapq.heappush(pq, arr[i+k])
    return arr

print(sortKSortedArray([9,8,7,19,18], 3))