
# Hoores partition - Time : O(n)
def segregateZeroAndOne(arr):
    lp, rp = -1, len(arr)
    while True:
        lp += 1
        while lp <= len(arr) - 1 and arr[lp] == 0:
            lp += 1
        
        rp -= 1
        while rp >= 0 and arr[rp] == 1:
            rp -= 1
        
        if lp >= rp:
            break
        arr[lp], arr[rp] = arr[rp], arr[lp]
    
    return arr

print(segregateZeroAndOne([0,1,1,1,0]))