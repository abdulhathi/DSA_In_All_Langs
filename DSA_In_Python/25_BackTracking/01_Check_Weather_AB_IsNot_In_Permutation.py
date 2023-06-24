

def permutation(s, c):
    
    def backtrack(s, i, n):
        if i == n-1 and c not in "".join(s):
            print(s)
            return
        for j in range(i, n):
            s[i], s[j] = s[j], s[i]
            backtrack(s, i+1, n)
            s[i], s[j] = s[j], s[i]
    
    backtrack(s, 0, len(s))

permutation(list("ABC"), "AB")
# print("ab" not in "abdul")