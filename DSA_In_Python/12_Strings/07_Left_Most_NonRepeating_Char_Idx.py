# Time : O(n) Space : O(1)
from collections import defaultdict

def leftMostNonRepeatCharIndex(s):
    dic = defaultdict(int)
    for c in s:
        dic[c] += 1
    for i in range(len(s)):
        if dic[s[i]] == 1:
            return i
    return -1

print(leftMostNonRepeatCharIndex("geeksforgeeks"))
print(leftMostNonRepeatCharIndex("abcabc"))
print(leftMostNonRepeatCharIndex("abcd"))