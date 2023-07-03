
# Time : O(logn) Space : O(1)
def findFirstOccurence(arr, x):
    lp, rp = 0, len(arr)-1
    
    while lp <= rp:
        mid = (lp+rp) // 2
        if x == arr[mid]:
            if mid == 0 or arr[mid-1] != arr[mid]:
                return mid
            rp = mid-1
        elif arr[mid] > x:
            rp = mid-1
        else:
            lp = mid+1
    return -1

print(findFirstOccurence([1,10,10,10,20,20,40], 20))
