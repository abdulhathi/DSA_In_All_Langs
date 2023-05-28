def weightedSumByRange(nums, rangeK):
    n, pSum, pWSum = len(nums), [nums[0]], [nums[0]]
    for i in range(1, n):
        pWSum.append(pWSum[i-1] + ((i+1)*nums[i]))
        pSum.append(pSum[i-1] + nums[i])
    
    print(pSum, pWSum)
    res = []
    for lp, rp in rangeK:
        if lp == 0:
            res.append(pWSum[rp])
        else:
            res.append(pWSum[rp] - pWSum[lp-1])
    return res
        
print(weightedSumByRange([2,3,5,4,6,1], [[0,2],[2,3]]))

