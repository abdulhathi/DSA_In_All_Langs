def checkSubsequence(s1, s2):
    i = 0
    for c in s2:
        for j in range(i, len(s1)):
            if s1[j] == c:
                i = j + 1
                break
        else:
            return False
    return True

print(checkSubsequence("ABCD","AD"))
print(checkSubsequence("ABCDE","AED"))

def checkSubsequence(s1, s2):
    i, j, m, n = 0, 0, len(s1), len(s2)
    while i < m and j < n:
        if s1[i] == s2[j]:
            j += 1
        i += 1
    return j == n

print(checkSubsequence("ABCD","AD"))
print(checkSubsequence("ABCDE","AED"))

# Time : O(n) Aux Space : O(n)
def checkSubsequence_Recursive(s1, s2, m, n):
    if n == 0:
        return True
    if m == 0:
        return False
    if s1[m-1] == s2[n-1]:
        return checkSubsequence_Recursive(s1, s2, m-1, n-1)
    else:
        return checkSubsequence_Recursive(s1, s2, m-1, n)
    
print(checkSubsequence_Recursive("ABCD","AD", 4, 2))
print(checkSubsequence_Recursive("ABCDE","AED", 5, 3))