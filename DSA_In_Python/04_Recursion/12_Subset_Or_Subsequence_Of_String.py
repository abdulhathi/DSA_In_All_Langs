
res = []
def subsetOfAString(s, curr, ind):
    if ind == len(s):
        res.append(curr)
        return
    subsetOfAString(s, curr, ind+1)
    subsetOfAString(s, curr+s[ind], ind+1)

subsetOfAString("ABC", "", 0)
print(res)