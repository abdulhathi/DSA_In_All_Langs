def searchAValAndRowAndColumnWiseSorted(mat, val):
    ROWS, COLS = len(mat), len(mat[0])
    r, c = 0, COLS-1
    while c >= 0 and r <= ROWS-1:
        if mat[r][c] > val:
            c -= 1
        elif mat[r][c] < val:
            r += 1
        else:
            return (r,c)
        
mat = [[10,20,30,40],
       [15,25,35,45],
       [27,29,37,48],
       [32,33,39,50]]
print(searchAValAndRowAndColumnWiseSorted(mat, 39))
