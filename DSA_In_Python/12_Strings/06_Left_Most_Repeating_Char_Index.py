# Dictionary Time : O(n) Space : O(1) - In One Iteration.
from collections import defaultdict
def leftMostRepeatingCharInd(s):
    dic = defaultdict(int)
    res = -1
    for i in range(len(s)-1, -1, -1):
        c = s[i]
        dic[c] += 1
        if dic[c] > 1:
            res = i
    print(dic)
    return res

print(leftMostRepeatingCharInd("geeksforgeeks"))
print(leftMostRepeatingCharInd("abbcc"))
print(leftMostRepeatingCharInd("abcd"))

