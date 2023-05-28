# Time : O(n) Space : O(1)
def subArrayWithGivenSum(nums, sumK):
    currSum = 0
    lp, rp = 0, 0
    while rp < len(nums) and lp < len(nums):
        if currSum == sumK:
            return True
        if currSum > sumK:
            currSum -= nums[lp]
            lp += 1
        else:
            currSum += nums[rp]
            rp += 1
    return True if currSum == sumK else False

print(subArrayWithGivenSum([1,4,20,3,10,5], 33))
print(subArrayWithGivenSum([1,4,0,0,3,10,5], 7))
print(subArrayWithGivenSum([2,4], 3))