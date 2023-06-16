# Time : O(n) Space : O(n)
def largestAreaInHistogram(histogram):
    n = len(histogram)
    pSEList, nSEList = [], [0] * n
    st = []
    # Finding prev closest smaller elem index
    for i, height in enumerate(histogram):
        while st and histogram[st[-1]] >= height:
            st.pop()
        pSE = st[-1] if st else -1
        pSEList.append(pSE)
        st.append(i)
    
    # Finding next closest smaller elem index
    st = []
    for i in range(n-1, -1, -1):
        height = histogram[i]
        while st and histogram[st[-1]] >= height:
            st.pop()
        nSE = st[-1] if st else n
        nSEList[i] = nSE
        st.append(i)

    # print(pSEList, nSEList)
    maxArea = 0
    for i, height in enumerate(histogram):
        curr = height
        curr += (i - pSEList[i] - 1) * height
        curr += (nSEList[i] - i - 1) * height
        maxArea = max(maxArea, curr)
    return maxArea

print(largestAreaInHistogram([6,2,5,4,1,5,6]))
