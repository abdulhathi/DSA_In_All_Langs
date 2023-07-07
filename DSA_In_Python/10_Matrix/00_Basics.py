ROWS, COLS = 3, 3
mat = [[0] * ROWS] * COLS

print(mat)

mat[0][0] = 1

print(mat)

mat1 = [[0] * ROWS for _ in range(COLS)]

print(mat1)

mat1[0][0] = 2
print(mat1)


for r in range(0, 9, 3):
    print(r)