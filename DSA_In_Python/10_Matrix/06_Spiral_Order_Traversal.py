# Time : O(m*n)
def spiralOrderTraversal(mat):
    ROWS, COLS = len(mat), len(mat[0])
    lp, tp, rp, bp = 0, 0, COLS-1, ROWS-1
    res = []

    while lp <= rp and tp <= bp:
        for c in range(lp, rp+1):
            res.append(mat[tp][c])
        tp += 1

        for r in range(tp, bp+1):
            res.append(mat[r][rp])
        rp -= 1

        if tp <= bp:
            for c in range(rp, lp-1, -1):
                res.append(mat[bp][c])
            bp -= 1
        
        if lp <= rp:
            for r in range(bp, tp-1, -1):
                res.append(mat[r][lp])
            lp += 1
    return res

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(spiralOrderTraversal(mat))