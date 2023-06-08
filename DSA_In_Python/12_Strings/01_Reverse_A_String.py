# Time : O(n) Space : O(n)
def reverseAString(s):
    res = ""
    for c in s:
        res = c + res

    return res

print(reverseAString("abdul"))


def reverseAString(s):
    return s[::-1]

print(reverseAString("hathi"))