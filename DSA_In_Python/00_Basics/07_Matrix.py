matrix = [[0,0],[0,1],[0,-1]]

matrix.sort()
print(matrix)


[[0, -1], [0, 0], [0, 1]]

mat = [[3,2,1],[1,7,6],[2,7,7]]
for col in zip(*mat):
    print(col)


"""
                |
                |
                |
                |
           0,-1 |0,0 
|   |   |   |   |   |   |   |   |   |   |
                |
                |
                |
                |
                | 

"""