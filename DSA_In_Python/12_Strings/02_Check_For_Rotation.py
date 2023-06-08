# Time : O(n) Aux Space : O(1)
def checkForRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1+s1)

print(checkForRotation("ABCD", "CDAB"))
print(checkForRotation("ABCD", "ABBA"))
print(checkForRotation("ABCD", "ABBAA"))