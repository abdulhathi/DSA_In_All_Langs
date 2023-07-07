
# Hoores partition - Time : O(n)
def segregateZerosOnesAndTwos(arr):
    lp, mp, rp = 0, 0, len(arr)-1

    while mp <= rp:
        if arr[mp] == 0:
            arr[lp], arr[mp] = arr[mp], arr[lp]
            lp, mp = lp+1, mp+1
        elif arr[mp] == 1:
            mp += 1
        else:
            arr[rp], arr[mp] = arr[mp], arr[rp]
            rp = rp-1
    return arr

print(segregateZerosOnesAndTwos([0,1,2,1,1,0,2]))

