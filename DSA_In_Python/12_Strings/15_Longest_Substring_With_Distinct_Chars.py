from collections import defaultdict

def longestSubStrWithDistinctChars(s):
    prev = defaultdict(int)
    maxLen, currLen = 0, 0
    for ind, char in enumerate(s):
        if char in prev:
            currLen = ind - prev[char]
        else:
            currLen += 1
        maxLen = max(currLen, maxLen)
        prev[char] = ind
    return maxLen

print(longestSubStrWithDistinctChars("abcadbd"))
print(longestSubStrWithDistinctChars("pwwkew"))

"""
     0 1 2 3 4 5 6
    "a b c a d b d"

    [a:3, b:1, c:2, d:4]

    i = 0 => "a"    maxLen = 1
    i = 1 => "b"    maxLen = 2
    i = 2 => "c"    maxLen = 3
    i = 3 => "a"    maxLen = max(3 - 0, 3) = 3
    i = 4 => "d"    maxLen = 4
    i = 5 => "b"    maxLen = max(5 - 1, 4) = 4
    i = 6 => "d"    maxLen = max(6 - 4, 4) = 4

     0 1 2 3 4 5
    "p w w k e w"

    [p:0, w:2, k:3]

    i = 0 => "p"    maxLen = 1
    i = 1 => "w"    maxLen = 2
    i = 2 => "w"    maxLen = (2 - 1, 2) = 2
    i = 3 => "k"    maxLen =
"""