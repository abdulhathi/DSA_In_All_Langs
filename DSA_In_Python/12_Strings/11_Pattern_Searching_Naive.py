
# Time : O(m*n)
def patternSearch(word, pat):
    i, j, m, n = 0, 0, len(word), len(pat)
    res = []
    while i < (m-n+1):
        k = i
        while k < m and j < n and word[k] == pat[j]:
            k, j = k+1, j+1
        if j == n:
            res.append(i)
            j = 0
        i += 1
    return res

print(patternSearch("geeks for geeks", "geeks"))


def imporvedNaivePatterSearch(word, pat):
    i, j, m, n = 0, 0, len(word), len(pat)
    res = []
    while i < (m-n+1):
        k = i
        while k < m and j < n and word[k] == pat[j]:
            k, j = k+1, j+1
        if j == n:
            res.append(i)
        i = i + (j if j > 0 else 1)
        j = 0
    return res

print(imporvedNaivePatterSearch("ABCABCD", "ABCD"))
print(imporvedNaivePatterSearch("ABCEABFABCD", "ABCD"))