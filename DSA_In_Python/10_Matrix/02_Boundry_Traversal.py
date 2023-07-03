# Time : O(r+e) Space : O(1)
def boundryTraversalOfMatrix(mat):
    lp, tp, rp, bp = 0, 0, len(mat[0])-1, len(mat)-1
    res = []
    # Left to right
    for c in range(lp, rp+1):
        res.append(mat[tp][c])
    tp += 1

    # Top to bottom
    for r in range(tp, bp+1):
        res.append(mat[r][rp])
    rp -= 1

    # Right to left
    if tp <= bp:
        for c in range(rp, lp-1, -1):
            res.append(mat[bp][c])
        bp -= 1
    
    # Bottom to top
    if lp <= rp:
        for r in range(bp, tp-1, -1):
            res.append(mat[r][lp])
        lp += 1

    return res

mat = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
print(boundryTraversalOfMatrix(mat))

mat1 = [
    [1,2,3,4],
    [5,6,7,8]]
print(boundryTraversalOfMatrix(mat1))

print(boundryTraversalOfMatrix([[1,2,3,4]]))
print(boundryTraversalOfMatrix([[1],[2],[3]]))
print(boundryTraversalOfMatrix([[1,2],[3,4],[5,6]]))