
def perm(s, i):
    if len(s)-1 == i:
        print(s)
        return
    for j in range(i, len(s)):
        s[i], s[j] = s[j], s[i]
        perm(s, i+1)
        s[i], s[j] = s[j], s[i]
    

s = list("ABC")
perm(s, 0)
# s[2] = "D"
# print(s)

