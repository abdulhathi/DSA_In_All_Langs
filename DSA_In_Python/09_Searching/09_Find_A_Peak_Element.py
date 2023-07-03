
def findAPeakElement(arr):
    lp, rp = 0, len(arr)-1
    while lp <= rp:
        mid = (lp+rp)//2
        if (mid == 0 or arr[mid-1] <= arr[mid]) and (mid == len(arr)-1 or arr[mid+1] <= arr[mid]):
            return mid
        elif mid > 0 and arr[mid-1] >= arr[mid]:
            rp = mid-1
        else:
            lp = mid+1
    return -1

print(findAPeakElement([5,10,20,15,7]))
print(findAPeakElement([10,20,15,5,23,90,67]))