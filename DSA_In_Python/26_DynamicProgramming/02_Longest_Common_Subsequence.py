from collections import defaultdict

# Dynamic programming top down Time : O(m*n) Space : O(m*n)
def lcsTopDown(s1, s2):
    memo = defaultdict(int)

    def dfs(m, n):
        if (m, n) in memo:
            return memo[(m,n)]
        if m == 0 or n == 0:
            memo[(m,n)] = 0
        elif s1[m-1] == s2[n-1]:
            memo[(m,n)] = 1 + dfs(m-1, n-1)
        else:
            memo[(m,n)] = max(dfs(m-1, n), dfs(m, n-1))
        return memo[(m,n)]
    
    return dfs(len(s1), len(s2))

print(lcsTopDown("AXYZ", "BAZ"))

def lcsBottomUp(s1, s2):
    tab = defaultdict(int)
    m, n = len(s1), len(s2)
    for r in range(1, m+1):
        for c in range(1, n+1):
            if s1[r-1] == s2[c-1]:
                tab[(r,c)] = 1 + tab[(r-1,c-1)]
            else:
                tab[(r,c)] = max(tab[(r-1,c)], tab[(r,c-1)])
    return tab[m,n]


print(lcsBottomUp("AXYZ", "BAZ"))