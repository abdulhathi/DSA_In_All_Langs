
def oddAppearElement(arr):
    res = arr[0]
    for i in range(1, len(arr)):
        res = res ^ arr[i]
    return res

print(oddAppearElement([4,4,7,4,8,7,7,7,8]))
