def maxProfit(nums):
  maxProfit = 0
  for i in range(1, len(nums)):
    if nums[i-1] < nums[i]:
      maxProfit += nums[i] - nums[i-1]
  return maxProfit

print(maxProfit([1,5,3,8,12]))