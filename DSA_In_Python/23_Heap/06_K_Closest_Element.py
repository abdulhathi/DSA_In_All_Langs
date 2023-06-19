import heapq

# Time : O(k logk) + O(n-k logk) + O(k)
def kClosestElement(nums, x, k):
    maxHeap = []
    for i in range(k):
        heapq.heappush(maxHeap, (-abs(nums[i] - x), nums[i]))

    for i in range(k, len(nums)):
        diff = abs(nums[i] - x)
        if -maxHeap[0][0] > diff:
            heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-diff, nums[i]))
    
    return [val for _, val in maxHeap]


print(kClosestElement([10,15,7,3,4], 8, 2))
print(kClosestElement([100,80,10,5,70], 2, 3))
print(kClosestElement([20,40,5,100,150], 100, 3))
"""
                (4,4)
        (2,0)               (1,2)        
"""