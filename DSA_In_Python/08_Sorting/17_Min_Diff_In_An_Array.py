import math

# Time : O(nlogn)
def minDiffInAnArray(arr):
    arr.sort()
    minDiff = math.inf
    for i in range(1, len(arr)):
        minDiff = min(minDiff, arr[i]-arr[i-1])
    return minDiff

print(minDiffInAnArray([1,8,12,5,18]))
print(minDiffInAnArray([8,15]))
print(minDiffInAnArray([8,-1,0,3]))
print(minDiffInAnArray([10]))