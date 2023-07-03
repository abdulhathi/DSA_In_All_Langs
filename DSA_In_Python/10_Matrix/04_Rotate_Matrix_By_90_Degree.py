def rotateMatrixBy90Degree(mat):
    R, C = len(mat), len(mat[0])
    res = [[0] * R for _ in range(C)]
    for r in range(R):
        for c in range(C):
            r1, c1 = abs(c-(R-1)), r
            res[r1][c1] = mat[r][c]
    return res

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(rotateMatrixBy90Degree(mat))

def rotateMatBy90Deg(mat):
    R, C = len(mat), len(mat[0])
    res = [[0] * R for _ in range(C)]

    for r in range(R):
        for c in range(C):
            res[abs(c-(R-1))][r] = mat[r][c]

    return res

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(rotateMatBy90Deg(mat))