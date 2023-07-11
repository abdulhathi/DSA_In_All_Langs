from collections import defaultdict

def longestPalindrome(s: str) -> str:
    dp = defaultdict(int)
    n = len(s)
    for i in range(n):
        dp[(i,i)] = 1
    r1,c1 = 0, 0
    for k in range(1,n):
        for r in range(n-k):
            c = r+k
            if s[r] == s[c] and (c-r == 1 or dp[(r+1,c-1)] == 1):
                dp[(r,c)] = 1
                if (c+1) - r > (c1+1) - r1:
                    r1, c1 = r, c
            else:
                dp[(r,c)] = 0
    return s[r1:c1+1]

# print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))