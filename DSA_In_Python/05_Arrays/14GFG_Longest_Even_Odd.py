# Python Time : (n) space : O(1)
def longestEvenOdd(nums):
    n = len(nums)
    isEven = nums[0] % 2 == 0
    maxLen, length = 1, 1
    for i in range(1, n):
        if (nums[i] % 2 == 0 and isEven) or (nums[i] % 2 != 0 and not isEven):
            maxLen = max(maxLen, length)
            length = 1
            isEven = nums[i] % 2 == 0
            continue
        length += 1
        isEven = not isEven
    
    return max(maxLen, length)

print(longestEvenOdd([10,12,14,7,8]))
print(longestEvenOdd([7,10,13,14]))
print(longestEvenOdd([10,12,8,4]))