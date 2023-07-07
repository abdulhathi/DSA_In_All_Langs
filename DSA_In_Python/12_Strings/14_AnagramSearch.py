from collections import defaultdict

# Time : O(m) Space : O(n)
def anagramSearch(text, pat):
    def isSameAsPat(textCount, patCount):
        for key in pat:
            if textCount[key] != patCount[key]:
                return False
        return True

    anagramCount, m, n = 0, len(text), len(pat)
    countText, countPat = defaultdict(int), defaultdict(int)
    for cT, cP in zip(text, pat):
        countText[cT] += 1
        countPat[cP] += 1
    
    if isSameAsPat(countText, countPat):
        anagramCount = 1
    
    for i in range(n, m):
        first, curr =text[i-n], text[i]
        countText[first] -= 1
        countText[curr] += 1

        if isSameAsPat(countText, countPat):
            anagramCount += 1

    return anagramCount

print(anagramSearch("geeksforgeeks", "frog"))
print(anagramSearch("ababcabcabababdababd", "ab"))