import math

def allocateMinPages(arr, j, k):
    if k == 1:
        return sum(arr[j:])
    res = math.inf
    sumVal = 0
    for i in range(j, len(arr)):
        sumVal += arr[i]
        res = min(res, max(sumVal, allocateMinPages(arr, i+1, k-1)))
    return res                    

# 10, 20, 30, 40

print(allocateMinPages([10,20,30,40], 0, 2))
print(allocateMinPages([10,20,30], 0, 1))
print(allocateMinPages([10,5,30,1,2,5,10,10], 0, 3))