# Stack Time : O(n) Space : O(n)
def reverseWordsInAString(s):
    st = []
    word = ""
    for c in s:
        if c == " ":
            st.append(word)
            word = ""
            continue
        word += c
    st.append(word)

    res = st.pop()
    while st:
        res += " " + st.pop() 
    return res

print(reverseWordsInAString("welcome to gfg"))