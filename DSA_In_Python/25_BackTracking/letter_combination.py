def genCombination(dA, dB):
    res = []
    for c1 in dA:
        for c2 in dB:
            res.append(c1+c2)
    return res

print(genCombination("abc", "def"))
print(genCombination(['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'], "ghi"))