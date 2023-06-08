# Naive method Time : O(n^2) Space : O(1)
def maxCircularSubArraySum(nums):
    n = len(nums)
    maxSum = 0
    for i in range(n):
        currSum = nums[i]
        currMaxSum = nums[i]
        for j in range(i+1, n+i):
            num = nums[j % n]
            currSum += num
            currMaxSum = max(currMaxSum, currSum)
        maxSum = max(maxSum, currMaxSum)
    return maxSum

print(maxCircularSubArraySum([5,-2,3,4]))

# Efficient method - Calculating (totalSum - MinSumSubArray) or maxSumSubArray
def maxCircularSubArraySum(nums):
    def maxSumSubArray(nums):
        prevSum, maxSum = nums[0], nums[0]
        for i in range(1, len(nums)):
            prevSum = max(prevSum + nums[i], nums[i])
            maxSum = max(maxSum, prevSum)
        return maxSum
    
    maxSum = maxSumSubArray(nums)
    if maxSum < 0:
        return maxSum
    totalSum = 0
    for i in range(len(nums)):
        totalSum += nums[i]
        nums[i] = -nums[i]
    minSum = -maxSumSubArray(nums)
    return max(maxSum, totalSum - minSum)

print(maxCircularSubArraySum([8,-4,3,-5,4])) 
