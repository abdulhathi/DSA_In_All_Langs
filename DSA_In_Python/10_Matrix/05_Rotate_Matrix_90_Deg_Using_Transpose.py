
# Time : O(n^2) Space : O(1)
def rotateMatBy90Deg(mat):
    # Transpose the matrix
    for r in range(len(mat)-1):
        for c in range(r+1, len(mat[0])):
            mat[r][c], mat[c][r] = mat[c][r], mat[r][c]

    # Reverse the matrix by row wise
    tp, bp = 0, len(mat)-1
    while tp < bp:
        mat[tp], mat[bp] = mat[bp], mat[tp]
        tp, bp = tp+1, bp-1
    
    return mat

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(rotateMatBy90Deg(mat))

mat1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(rotateMatBy90Deg(mat1))