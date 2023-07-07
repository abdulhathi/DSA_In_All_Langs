
# Time : O(n^2)
def cycleSort(arr):
    n = len(arr)
    for cs in range(n):
        item = arr[cs]
        pos = cs
        for i in range(cs+1, n):
            if arr[i] < item:
                pos += 1
        # if pos == cs:
        #     continue
        arr[pos], item = item, arr[pos]
        while pos != cs:
            pos = cs
            for i in range(cs+1, n):
                if arr[i] < item:
                    pos += 1
            # if pos == cs:
            #     continue
            arr[pos], item = item, arr[pos]
    return arr

print(cycleSort([20,40,50,10,30]))
print(cycleSort([10, 8, 20, 5]))