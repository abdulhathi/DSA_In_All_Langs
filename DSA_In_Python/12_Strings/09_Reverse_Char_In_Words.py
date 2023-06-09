def reverseCharsInWords(s):
    s = list(s)
    def reverseWord(s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1
    
    l, r = 0, 0
    for i, c in enumerate(s):
        if c == " ":
            reverseWord(s, l, r)
            l = i + 1
            continue
        r = i
    reverseWord(s, l, r)

    reverseWord(s, 0, len(s)-1)
    return "".join(s)


print(reverseCharsInWords("welcome to dsa"))