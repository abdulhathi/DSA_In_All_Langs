# Time : O(n) Space :O(n)
def nextGreaterElement(nums):
    n = len(nums)
    res, st = [0] * n, []

    for i in range(n-1, -1, -1):
        num = nums[i]
        while st and nums[st[-1]] <= num:
            st.pop()
        nGE = nums[st[-1]] if st else -1
        st.append(i)
        res[i] = nGE
    return res

print(nextGreaterElement([5,15,10,8,6,12,7]))
print(nextGreaterElement([10,15,20,25]))
print(nextGreaterElement([25,20,15,10]))