from collections import defaultdict

# Convert "S1" to "S2"
def editDistance(s1, s2):
    dp = defaultdict(int)

    def topDown(m, n):
        if (m, n) in dp:
            return dp[(m,n)]
        if m == 0:
            dp[(m,n)] = n
        elif n == 0:
            dp[(m,n)] = m
        elif s1[m-1] == s2[n-1]:
            dp[(m,n)] = topDown(m-1, n-1)
        else:
            dp[(m,n)] = 1 + min(topDown(m, n-1), topDown(m-1, n), topDown(m-1, n-1))
        
        return dp[(m,n)]
    
    return topDown(len(s1), len(s2))

print(editDistance("saturday", "sunday"))
print(editDistance("cat", "cut"))

def editDistance_BottomUp(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for c in range(m+1):
        dp[0][c] = c
    for r in range(n+1):
        dp[r][0] = r

    # print(dp)
    for r in range(1, n+1):
        for c in range(1, m+1):
            if s2[r-1] == s1[c-1]:
                dp[r][c] = dp[r-1][c-1]
            else:
                dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
    return dp[n][m]

print(editDistance_BottomUp("saturday", "sunday"))
