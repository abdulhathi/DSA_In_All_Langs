# Naive Method Time : O(n^2) Space : O(1)
def maxSumSubArray(nums):
    n = len(nums)
    maxSum = nums[0]
    maxSumInd = [0, 0]
    for i in range(n):
        currSum = 0
        for j in range(i, n):
            currSum += nums[j]
            if currSum > maxSum:
                maxSum = currSum
                maxSumInd = [i, j]
    return maxSum, maxSumInd

print(maxSumSubArray([1,-2,3,-1,2]))

# Efficient Method 
def maxSumSubArray(nums):
    maxSum = nums[0]
    prevSum = nums[0]
    for i in range(1, len(nums)):
        prevSum = max(prevSum + nums[i], nums[i])
        maxSum = max(maxSum, prevSum)
    return maxSum

print(maxSumSubArray([1,-2,3,-1,2]))