# Naive : Sorting : Time - O(nlogn)
def checkAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

print(checkAnagram("listen", "silent"))
print(checkAnagram("aabca", "acaba"))
print(checkAnagram("axy", "azy"))

# Optimized : Dictionary : Time - O(n) Space - O(1)
from collections import defaultdict

def checkAnagram_Optimized(s1, s2):
    if len(s1) != len(s2):
        return False
    dic = defaultdict(int)
    for c1, c2 in zip(s1, s2):
        dic[c1] += 1
        dic[c2] -= 1

    for count in dic.values():
        if count != 0:
            return False
    return True

print(checkAnagram_Optimized("listen", "silent"))
print(checkAnagram_Optimized("aabca", "acaba"))
print(checkAnagram_Optimized("axy", "azy"))