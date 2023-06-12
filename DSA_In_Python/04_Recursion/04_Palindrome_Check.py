# Time : O(n) Aux Space : O(n)
def palindrome(s):
    def isPal(s, lp, rp):
        if lp >= rp:
            return True
        if s[lp] != s[rp]:
            return False
        return isPal(s, lp+1, rp-1)
    
    return isPal(s, 0, len(s)-1)

print(palindrome("abbcbba"))
print(palindrome("abbcbbaa"))
print(palindrome("abbcdbba"))