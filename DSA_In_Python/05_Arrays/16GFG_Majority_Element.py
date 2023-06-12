# Python Naive method
def majorityElement(nums):
    n = len(nums)
    for i in range(n):
        cnt = 1
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                cnt += 1
            if cnt > (n // 2):
                return i
    return -1

print(majorityElement([8,7,6,8,6,6,6,6]))

# 1,8,2,8,3,8,4,8
# The majority element if exist the element must exist more than half in the array
# Time : O(n) space : O(1)
def majorityElement(nums):
    ind, cnt = 0, 1
    for i in range(1, len(nums)):
        if nums[ind] == nums[i]:
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            ind = i
            cnt = 1
    
    cnt = 0
    for num in nums:
        if num == nums[ind]:
            cnt += 1
        if cnt > (len(nums) // 2):
            return ind
    return -1

print(majorityElement([8,7,6,8,6,6,6,6]))

