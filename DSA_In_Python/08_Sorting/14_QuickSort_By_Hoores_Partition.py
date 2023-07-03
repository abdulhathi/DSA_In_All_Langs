
def quickSortByHoores(arr):
    def partition(l, h):
        pivot = arr[l]
        lp, rp = l-1, h+1
        while True:
            lp += 1
            while lp <= h and arr[lp] < pivot:
                lp += 1
            rp -= 1
            while rp >= l and arr[rp] > pivot:
                rp -= 1
            if lp >= rp:
                return rp
            arr[lp], arr[rp] = arr[rp], arr[lp]
    
    def divide(l, h):
        if l < h:
            p = partition(l, h)
            divide(l, p)
            divide(p+1, h)
    
    divide(0, len(arr)-1)
    return arr

print(quickSortByHoores([8,4,7,9,3,10,5]))