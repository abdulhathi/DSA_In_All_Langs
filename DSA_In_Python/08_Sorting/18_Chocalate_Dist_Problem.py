import math

# Time : O(nlogn)
def chocalateDistProblem(chocs, kids):
    if len(chocs) < kids:
        return -1
    chocs.sort()
    minDiff = math.inf
    for i in range(len(chocs)-kids+1):
        minDiff = min(minDiff, chocs[i+kids-1] - chocs[i])
    return minDiff

print(chocalateDistProblem([7,3,2,4,9,12,56], 3))
print(chocalateDistProblem([3,4,1,9,56,7,9,12], 5))
