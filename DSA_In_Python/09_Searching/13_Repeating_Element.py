

def repeatingElement(arr):
    for i in range(len(arr)):
        arr[i] += 1
    s, f = arr[0], arr[0]

    s, f = arr[s], arr[arr[f]]
    while s != f:
        s, f = arr[s], arr[arr[f]]
    s = arr[0]
    while s != f:
        s, f = arr[s], arr[f]
    return s-1


print(repeatingElement([0,2,1,3,2,2]))

