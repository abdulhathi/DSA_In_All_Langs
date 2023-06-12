res = []
def printOneToN(n):
    if n == 0:
        return
    printOneToN(n-1)
    res.append(n)

printOneToN(5)
print(res)