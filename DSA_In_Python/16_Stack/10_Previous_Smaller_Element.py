
def prevSmallerElement(nums):
    res, st = [], []
    for i, num in enumerate(nums):
        while st and nums[st[-1]] >= num:
            st.pop()
        nSE = nums[st[-1]] if st else -1
        res.append(nSE)
        st.append(i)
    return res

print(prevSmallerElement([6,2,5,4,1,5,6]))