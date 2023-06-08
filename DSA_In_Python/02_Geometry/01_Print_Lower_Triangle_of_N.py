# Print lower triangle with alternate ‘*’ and ‘#’
# https://www.geeksforgeeks.org/print-lower-triangle-with-alternate-and/

def printLowerTriangle(n):
    res = []
    for i in range(n):
        row = []
        for j in range(i+1):
            row.append("#" if (j+1) % 2 == 0 else "*")
        res.append(row)
    return res

print(printLowerTriangle(5))