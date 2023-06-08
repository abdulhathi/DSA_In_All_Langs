# Selecting minValue i to n-1 in every pass and Swap the minvalu
def selectionSort(nums):
    n = len(nums)
    for i in range(n-1):
        minInd = i
        for j in range(i+1, n):
            if nums[j] < nums[minInd]:
                minInd = j
        nums[i], nums[minInd] = nums[minInd], nums[i]
    return nums

print(selectionSort([10,5,8,20,2,18]))