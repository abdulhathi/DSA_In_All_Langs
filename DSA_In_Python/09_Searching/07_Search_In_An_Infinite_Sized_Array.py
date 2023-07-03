

def searchInfiniteSizedArray(arr, x):
    lp, rp = 0, x
    while lp <= rp:
        mid = (lp+rp)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            rp = mid-1
        else:
            lp = mid+1
    return -1

arr = [i for i in range(10000)]
arr.remove(10)
print(arr)
print(searchInfiniteSizedArray(arr, 10))