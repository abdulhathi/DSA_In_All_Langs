
# Time : O(n^2) Space : O(n)
def longestIncreasingSubsequence(nums):
    lis = [1] * len(nums)

    res = 1
    for rp, curr in enumerate(nums): 
        maxLis = 0
        for lp in range(rp):
            prev = nums[lp]
            if prev <= curr:
                maxLis = max(lis[lp], maxLis)
        lis[rp] += maxLis
        res = max(res, lis[rp])
    return res

print(longestIncreasingSubsequence([10,9,2,5,3,7,101,18]))

