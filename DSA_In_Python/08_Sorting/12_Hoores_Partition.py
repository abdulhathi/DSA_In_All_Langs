
def hooresPartition(arr, l, h):
    pivot = arr[l]
    lp, rp = l-1, h+1
    while True:
        lp += 1
        while lp <= h and arr[lp] < pivot:
            lp += 1
        rp -= 1
        while rp >= l and arr[rp] > pivot:
            rp -= 1
        if lp >= rp:
            return rp, arr
        arr[lp], arr[rp] = arr[rp], arr[lp]

print(hooresPartition([5,3,8,4,2,7,1,10], 0, 7))