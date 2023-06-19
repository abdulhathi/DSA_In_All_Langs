# Time O(m*(n+n)) Space : O(n)
def largestRectAreaOfAllOnes(matrix):
    def getMaxArea(histogram):
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

    R, C = len(matrix), len(matrix[0])
    histogram = [0] * C
    maxArea = 0
    for r in range(R):
        for c in range(C):
            histogram[c] = histogram[c] + 1 if matrix[r][c] == 1 else 0
        maxArea = max(getMaxArea(histogram), maxArea)
    
    return maxArea


print(largestRectAreaOfAllOnes([[0,1,1,0],[1,1,1,1],[1,1,1,1],[1,1,0,0]]))
