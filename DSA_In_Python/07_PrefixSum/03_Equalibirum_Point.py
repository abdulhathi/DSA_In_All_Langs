# Time : O(n) Space : O(n)
def equalibirumPoint(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    sSum = [0] * n
    pSum = [nums[0]]
    sSum[n-1] = nums[n-1]
    for i in range(1, n):
        pSum.append(pSum[i-1] + nums[i])
    
    for i in range(n-2, -1, -1):
        sSum[i] = sSum[i+1] + nums[i]

    if sSum[1] == 0:
        return nums[0]
    if pSum[n-2] == 0:
        return nums[n-1]
    
    for i in range(1, n-1):
        if pSum[i-1] == sSum[i+1]:
            return nums[i]
    return None

print(equalibirumPoint([3,4,8,-9,20,6]))
print(equalibirumPoint([4,2,-2]))
print(equalibirumPoint([4,2,2]))

# More Efficeint solution

def eqPoint(nums):
    ls, rs = 0, sum(nums)
    for num in nums:
        rs -= num
        if ls == rs:
            return num
        ls += num
    return None

print(eqPoint([3,4,8,-9,20,6]))
print(eqPoint([4,2,-2]))
print(eqPoint([4,2,2]))