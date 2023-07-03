
def lomutoPartition(arr):
    n = len(arr)
    pivot = arr[n-1]
    i = -1
    for j in range(n):
        if arr[j] <= pivot:
            arr[i+1], arr[j] = arr[j], arr[i+1]
            i += 1
    return i, arr

print(lomutoPartition([10,80,30,90,50,70]))