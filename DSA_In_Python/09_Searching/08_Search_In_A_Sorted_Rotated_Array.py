# Time : O(logn)
def searchInSortedRotatedArray(arr, x):
    lp, rp = 0, len(arr)-1
    while lp <= rp:
        mid = (lp+rp) // 2
        if arr[mid] == x:
            return mid
        elif arr[lp] <= arr[mid]:
            if mid == 0 or not arr[lp] <= x <= arr[mid-1]:
                lp = mid+1
            else:
                rp = mid-1
        else:
            if mid == len(arr)-1 or arr[mid+1] <= x <= arr[rp]:
                rp = mid-1
            else:
                lp = mid+1
    return -1

print(searchInSortedRotatedArray([10,20,30,40,50,8,9], 8))