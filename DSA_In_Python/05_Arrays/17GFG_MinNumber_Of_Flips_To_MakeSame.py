# Time : O(n) Space : O(n)
def minNumOfFlips(binary):
    i, n = 0, len(binary)
    zR, oR = [], []
    while i < n:
        if binary[i] == 1:
            oR.append([i, i])
            while i < n and binary[i] == 1:
                oR[len(oR)-1][1] = i
                i += 1
        else:
            zR.append([i, i])
            while i < n and binary[i] == 0:
                zR[len(zR)-1][1] = i
                i += 1
    return zR if len(zR) < len(oR) else oR

print(minNumOfFlips([1,1,0,0,0,1]))
print(minNumOfFlips([1,0,0,0,1,0,0,1,1,1,1]))

# Time : O(n) Space : O(1)
def minNumOfFlips(binary):
    n = len(binary)
    flipRange = []
    for i in range(1, n):
        if binary[i] == binary[i-1]:
            continue
        if binary[i] != binary[0]:
            flipRange.append([i, i])
        else:
            flipRange[len(flipRange)-1][1] = i - 1
    return flipRange
        
print(minNumOfFlips([1,1,0,0,0,1]))
print(minNumOfFlips([1,0,0,0,1,0,0,1,1,1,1]))