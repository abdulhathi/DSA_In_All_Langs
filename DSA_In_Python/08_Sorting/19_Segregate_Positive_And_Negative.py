
# Hooers partition - Time : O(n)
def segregatePositiveAndNegative(arr):
    lp, rp = -1, len(arr)
    while True:
        lp += 1
        while lp <= len(arr)-1 and arr[lp] < 0:
            lp += 1
        rp -= 1
        while rp >= 0 and arr[rp] >= 0:
            rp -= 1
        if lp >= rp:
            break
        arr[lp], arr[rp] = arr[rp], arr[lp]
    
    return arr

print(segregatePositiveAndNegative([15,-3,-2,18]))
print(segregatePositiveAndNegative([15,-3,-2,18]))