import math

# Time : O(n) Space : O(1)
def findMaxSumOfKConsecElem(nums, k):
    maxSum, currSum = -math.inf, nums[0]
    for i in range(1, k):
        currSum += nums[i]
    
    maxSum = max(maxSum, currSum)
    for i in range(k, len(nums)):
        currSum -= nums[i-k]
        currSum += nums[i]
        maxSum = max(currSum, maxSum)

    return -1 if maxSum == -math.inf else maxSum

print(findMaxSumOfKConsecElem([1, 8, 30, -5, 20, 7], 3))
print(findMaxSumOfKConsecElem([5, -10, 6, 90, 3], 2))