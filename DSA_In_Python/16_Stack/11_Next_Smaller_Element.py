
def nextSmallerElement(nums):
    n = len(nums)
    res, st = [0] * n, []
    for i in range(n-1, -1, -1):
        num = nums[i]
        while st and nums[st[-1]] >= num:
            st.pop()
        nGE = nums[st[-1]] if st else -1
        res[i] = nGE
        st.append(i)
    return res

print(nextSmallerElement([6,2,5,4,1,5,6]))