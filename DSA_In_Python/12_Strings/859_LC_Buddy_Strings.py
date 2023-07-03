
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        lp, rp = 0, len(s)-1
        swapCount = 0
        while lp < rp:
            if s[lp] == goal[rp] and s[rp] == goal[lp]:
                if swapCount >= 1:
                    return False
                swapCount += 1
                if (s[0:lp] + s[rp] + s[lp+1:rp] + s[lp] + s[rp+1:]) == goal:
                    return True
                lp, rp = lp+1, rp-1
                continue
            if s[lp] == goal[lp] or s[rp] == goal[rp]:
                if s[lp] == goal[lp]:
                    lp += 1
                    continue
                if s[rp] == goal[rp]:
                    rp -= 1
                    continue
            else:
                return False

        return swapCount == 1

print(Solution().buddyStrings("ab","ba"))
print(Solution().buddyStrings("ab","ab"))
print(Solution().buddyStrings("aa","aa"))
print(Solution().buddyStrings("adcb","bcda"))
print(Solution().buddyStrings("abcd","badc"))
print(Solution().buddyStrings("abab","abab"))
print(Solution().buddyStrings("aaaaaaabc","aaaaaaacb"))