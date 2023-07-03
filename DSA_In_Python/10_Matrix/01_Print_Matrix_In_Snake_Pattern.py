# Time : O(m*n) Space : O(1)
def printSnackPattern(mat):
    res = []
    for ind, row in enumerate(mat):
        lp, rp, inc = 0, len(mat), 1
        if ind % 2 != 0:
            lp, rp, inc = len(mat)-1, -1, -1
        for i in range(lp, rp, inc):
            res.append(row[i])

    return res

print(printSnackPattern([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
