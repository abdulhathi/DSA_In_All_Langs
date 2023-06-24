def subsetSum(nums, target):
    def generateSubsets(nums, subset, n):
        if n == 0:
            return 1 if sum(subset) == target else 0
        res = generateSubsets(nums, subset, n-1)
        res += generateSubsets(nums, subset + [nums[n-1]], n-1)
        return res

    return generateSubsets(nums, [], len(nums))

print(subsetSum([10,20,15,5,10], 25))

