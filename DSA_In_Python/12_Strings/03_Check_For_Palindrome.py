# Time : O(n) Aux Space : O(1)
def checkForPalindrome(s):
    lp, rp = 0, len(s)-1
    while lp < rp:
        if s[lp] != s[rp]:
            return False
        lp, rp = lp+1, rp-1
    return True

print(checkForPalindrome("abba"))
print(checkForPalindrome("abbba"))
print(checkForPalindrome("abcba"))
print(checkForPalindrome("abdul"))
print(checkForPalindrome("a"))
print(checkForPalindrome("abA"))

def checkForPalindrome(s):
    return s == s[::-1]

print(checkForPalindrome("abba"))
print(checkForPalindrome("abbba"))
print(checkForPalindrome("abcba"))
print(checkForPalindrome("abdul"))
print(checkForPalindrome("a"))
print(checkForPalindrome("abA"))
