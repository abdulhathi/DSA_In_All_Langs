

def KMPAlgorithm(s, pat):
    m, n = len(s), len(pat)
    lps = [0] * n

    # Prepare LPS table.
    lp = 0
    for rp in range(1, n):
        if pat[lp] == pat[rp]:
            lps[rp] = lp + 1
            lp += 1
        else:
            lp = 0

    patCount, i, j = 0, 0, -1
    while i < m:
        if j == n-1:
            patCount += 1
            j = lps[j] - 1
            continue

        if s[i] == pat[j+1]:
            i, j = i+1, j+1
        elif j > -1:
            j = lps[j] - 1
        elif j == -1:
            i = i+1

    return patCount + (1 if j == n-1 else 0)

print(KMPAlgorithm("ababcabcabababdababd", "ababd"))
