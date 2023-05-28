# Naive solution TIME : O(n^2) SPACE : O(1)
def maxDiff(nums):
  n = len(nums)
  maxDiff = nums[1] - nums[0]
  for i in range(n-1):
    for j in range(i+1, n):
      maxDiff = max(maxDiff, nums[j] - nums[i])
  return maxDiff

print(maxDiff([2,3,10,6,4,8,1]))

# Optimal solution TIME : O(n) SPACE : O(1)
def maxDiff(nums):
  n = len(nums)
  maxDiff, minVal = nums[1] - nums[0], nums[0]
  for i in range(1, n):
    maxDiff = max(nums[i] - minVal, maxDiff)
    minVal = min(minVal, nums[i])
  return maxDiff

print(maxDiff([2,3,10,6,4,8,1]))
