# Find Kth smallest element by Lumoto partition
# Quick select
# Time : O(nlogn) Space : O(1)
def kthSmallestElement(arr, k):
    def partition(l, h):
        pivot = arr[h]
        lp = l-1
        for rp in range(l, h+1):
            if arr[rp] <= pivot:
                arr[lp+1], arr[rp] = arr[rp], arr[lp+1]
                lp += 1
        return lp
    
    l, h = 0, len(arr)-1
    while l <= h:
        p = partition(l, h)
        if p == k-1:
            return p, arr[p]
        elif p > k-1:
            h = p-1
        else:
            l = p+1
    return -1,-1

print(kthSmallestElement([10,4,5,8,11,6,26], 5))