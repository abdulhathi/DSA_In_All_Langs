
def countNumberOfOccInOne(arr):
    lp, rp = 0, len(arr)-1
    firstOcc = 0
    while lp <= rp:
        mid = (lp+rp)//2
        if arr[mid] == 1:
            if mid == 0 or arr[mid-1] != arr[mid]:
                firstOcc = mid
            rp = mid-1
        else:
            lp = mid+1
    
    return abs(len(arr) - firstOcc)

print(countNumberOfOccInOne([0,0,0,0,1,1,1,1,1,1]))
