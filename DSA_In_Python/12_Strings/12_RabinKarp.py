# Time : O((m-n+1)*n)
def rabinKarp(word, pat):
    d = 256
    m, n = len(word), len(pat)
    wordHash, patHash = 0, 0
    for i in range(n):
        patHash += ord(pat[i]) * d**(n-(i+1))
        wordHash += ord(word[i]) * d**(n-(i+1))
    
    res = []
    for i in range(m-n+1):
        if wordHash == patHash:
            for j in range(n):
                if pat[j] != word[j+i]:
                    break
            else:
                res.append(i)
        k = i+n
        if k >= m:
            continue
        wordHash = wordHash - (ord(word[i]) * d**(n-1))
        wordHash = d * wordHash
        wordHash = wordHash + ord(word[k])
    return res

print(rabinKarp("abdabcbabc", "abc"))