# Time : O(3^n)
def ropeCutting(l,a,b,c):
    if l < 0:
        return -1
    if l == 0:
        return 0
    res = max(ropeCutting(l-a,a,b,c), ropeCutting(l-b,a,b,c), ropeCutting(l-c,a,b,c))
    if res == -1:
        return -1
    return res + 1

print(ropeCutting(5,2,5,1))
print(ropeCutting(23,11,9,12))
print(ropeCutting(9,2,2,2))

