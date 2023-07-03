
# Time : O(logn) Space : O(1)
def indexOfLastOccurence(arr, x):
    lp, rp = 0, len(arr)-1
    while lp <= rp:
        mid = (lp+rp) // 2
        if arr[mid] == x:
            if mid == len(arr)-1 or arr[mid] != arr[mid+1]:
                return mid
            lp = mid+1
        elif arr[mid] > x:
            rp = mid-1
        else:
            lp = mid+1
    return -1

print(indexOfLastOccurence([10,15,20,20,40,40], 40))