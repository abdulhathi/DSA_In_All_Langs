# Naive Method Time : O(n^2) Space : O(1)
def trappingRainWater(bars):
    n = len(bars)
    res = 0
    for i in range(1, n-1):
        lMax, rMax = bars[i], bars[i]
        for j in range(0, i):
            lMax = max(lMax, bars[j])
        for j in range(i+1, n):
            rMax = max(rMax, bars[j])
        res += min(lMax, rMax) - bars[i]
    return res

print(trappingRainWater([3,0,1,2,5]))
print(trappingRainWater([5,0,6,2,3]))

# Optimized method using Precomputing Time : O(n) Space : O(n)
def trappingRainWater(bars):
    # Pre computing lMax and rMax
    n = len(bars)
    res = 0
    lMax, rMax = [0] * n, [0] * n
    lMax[0], rMax[n-1] = bars[0], bars[n-1]
    for i in range(1, n):
        lMax[i] = max(lMax[i-1], bars[i])
    for i in range(n-2, -1, -1):
        rMax[i] = max(rMax[i+1], bars[i])
    for i in range(1, n-1):
        res += min(lMax[i], rMax[i]) - bars[i]
    return res

print(trappingRainWater([3,0,1,2,5]))
print(trappingRainWater([5,0,6,2,3]))