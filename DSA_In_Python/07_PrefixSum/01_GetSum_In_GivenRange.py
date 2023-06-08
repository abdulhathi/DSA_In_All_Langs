# Time : O(n) Space : O(n)
def getSumInGivenRange(nums, rangeK):
    pSum = [nums[0]]
    for i in range(1, len(nums)):
        pSum.append(pSum[i-1] + nums[i])
    res = []
    for lp, rp in rangeK:
        rangeSum = pSum[rp] - (pSum[lp-1] if lp > 0 else 0)
        res.append(rangeSum)
    return res

print(getSumInGivenRange([2,8,3,9,6,5,4], [[0, 2],[1,3],[2,6]]))

# Givern sum : [2, 8, 3, 9, 6, 5, 4]
# Prefix sum : [2,10,13,22,28,33,37]
