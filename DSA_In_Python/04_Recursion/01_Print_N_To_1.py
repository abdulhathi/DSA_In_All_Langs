
# Time : O(n) Space : O(n)
res = []
def printNToOne_Recursively(n):
    if n == 0:
        return res
    res.append(n)
    return printNToOne_Recursively(n-1)

print(printNToOne_Recursively(5))

