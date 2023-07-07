
# Hoores partition
# Time : O(n)
def segregateEvenAndOdd(arr):
    lp, rp = -1, len(arr)
    while True:
        lp += 1
        while lp <= len(arr)-1 and arr[lp] % 2 == 0:
            lp += 1
        rp -= 1
        while rp >= 0 and arr[rp] % 2 != 0:
            rp -= 1
        if lp >= rp:
            break
        arr[lp], arr[rp] = arr[rp], arr[lp]
    
    return arr

print(segregateEvenAndOdd([15,14,13,12]))
