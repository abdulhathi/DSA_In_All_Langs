
# Time : O(nlogn) space : O(1)
def quickSortByLumoto(arr):
    def partition(l, h):
        pivot = arr[h]
        lp = l-1
        for rp in range(l, h+1):
            if arr[rp] <= pivot:
                arr[lp+1], arr[rp] = arr[rp], arr[lp+1]
                lp += 1
        return lp

    def divide(l, h):
        if l < h:
            p = partition(l, h)
            divide(l, p-1)
            divide(p+1, h)

    divide(0, len(arr)-1)
    return arr

print(quickSortByLumoto([8,4,7,9,3,10,5]))
