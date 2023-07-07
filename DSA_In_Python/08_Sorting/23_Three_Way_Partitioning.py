
# 
def threeWayPartitioning(arr, pivot):
    lp, mp, rp = 0, 0, len(arr)-1
    while mp <= rp:
        if arr[mp] < pivot:
            arr[lp], arr[mp] = arr[mp], arr[lp]
            lp, mp = lp+1, mp+1
        elif arr[mp] == pivot:
            mp += 1
        else:
            arr[mp], arr[rp] = arr[rp], arr[mp]
            rp -= 1
    return arr

print(threeWayPartitioning([2,1,2,20,10,20,1], 2))