

def findAPairUsingTwoPointerInSortedArray(arr, x):
    lp, rp = 0, len(arr)-1
    while lp < rp:
        sumVal = arr[lp]+arr[rp]
        if sumVal == x:
            return (lp, rp)
        elif sumVal > x:
            rp -= 1
        else:
            lp += 1
    return (-1,-1)

print(findAPairUsingTwoPointerInSortedArray([2,5,8,12,30], 17))