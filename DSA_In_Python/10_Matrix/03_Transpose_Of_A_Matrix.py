# Time : O(m*n)
def transposeOfAMatrix(mat):
    R, C = len(mat), len(mat[0])
    for r in range(R-1):
        for c in range(r+1, C):
            mat[r][c], mat[c][r] = mat[c][r], mat[r][c]
    
    return mat

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(transposeOfAMatrix(matrix))