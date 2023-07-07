

def patternSearching(word, pat):
    res = []
    pos = word.find(pat, 0)
    while pos >= 0:
        res.append(pos)
        # pos = -1
        pos = word.find(pat, pos+1)
    return res

print(patternSearching("geeks for geeks", "geeks"))