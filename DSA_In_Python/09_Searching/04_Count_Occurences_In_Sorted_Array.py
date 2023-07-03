
# Time : O(logn) Space : O(1)
def countOccurencesInSortedArray(arr, x):
    lp, rp = 0, len(arr)-1
    firstOcc, lastOcc = -1, -1
    while lp <= rp:
        mid = (lp+rp) // 2
        if arr[mid] == x:
            if mid == 0 or arr[mid-1] != arr[mid]:
                firstOcc = mid
            rp = mid-1
        elif arr[mid] > x:
            rp = mid-1
        else:
            lp = mid+1
    
    lp, rp = 0, len(arr)-1
    while lp <= rp:
        mid = (lp+rp) // 2
        if arr[mid] == x:
            if mid == len(arr)-1 or arr[mid+1] != arr[mid]:
                lastOcc = mid
            lp = mid+1
        elif arr[mid] > x:
            rp = mid-1
        else:
            lp = mid+1
    return abs(firstOcc - (lastOcc+1)) 

print(countOccurencesInSortedArray([20,20,20,20,20,20,30,30],20))