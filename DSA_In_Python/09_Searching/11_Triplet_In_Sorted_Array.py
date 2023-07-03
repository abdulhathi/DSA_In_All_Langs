
def tripletInSortedArray(arr, x):
    for i in range(len(arr)):
        lp, rp = i+1, len(arr)-1
        while lp < rp:
            sumVal = arr[i] + arr[lp] + arr[rp]
            if sumVal == x:
                return (i, lp, rp)
            elif sumVal > x:
                rp -= 1
            else:
                lp += 1
    return (-1,-1,-1)

print(tripletInSortedArray([2,3,4,8,9,20,40], 32))
print(tripletInSortedArray([1,2,5,6], 14))
