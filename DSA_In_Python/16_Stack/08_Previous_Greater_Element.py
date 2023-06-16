# Time : O(n) Space : O(n)
def prevGreaterElement(nums):
    res, st = [], []
    for i,num in enumerate(nums):
        while st and nums[st[-1]] <= num:
            st.pop()
        pG = nums[st[-1]] if st else -1
        res.append(pG)
        st.append(i)
    return res

print(prevGreaterElement([15,10,18,12,4,6,2,8]))
print(prevGreaterElement([8,10,12]))
print(prevGreaterElement([12,10,8]))