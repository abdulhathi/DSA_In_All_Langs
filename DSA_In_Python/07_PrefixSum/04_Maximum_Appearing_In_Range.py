# Time : O(n) Space : O(1)
def maxAppearingInRange(start, end):
    freq = [0] * 101
    n = len(start)
    for i in range(n):
        freq[start[i]] += 1
        freq[end[i]+1] -= 1

    maxApprCnt, maxApprElem = 0, None
    for i in range(1, 101):
        freq[i] = freq[i-1] + freq[i]
        if freq[i] > maxApprCnt:
            maxApprCnt = freq[i]
            maxApprElem = i
    return maxApprElem

print(maxAppearingInRange([1,2,4], [4,5,7]))
    