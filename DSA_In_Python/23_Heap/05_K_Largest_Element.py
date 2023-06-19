import heapq

def kLargestElement(nums, k):
    minHeap = []
    for i in range(k):
        heapq.heappush(minHeap, nums[i])
    
    for i in range(k, len(nums)):
        if minHeap[0] < nums[i]:
            heapq.heappop(minHeap)
            heapq.heappush(minHeap, nums[i])
    
    return minHeap

print(kLargestElement([5,15,10,20,8], 2))
print(kLargestElement([8,6,4,10,9], 3))
print(kLargestElement([5,15,10,20,8,25,18], 3))
"""
                (15)
        (20)    
"""