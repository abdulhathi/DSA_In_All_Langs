
# Time : O(nlogn)
def meetingMaxGuests(arr, dep):
    arr.sort()
    dep.sort()
    i, j = 0, 0
    count, maxGuest = 0, 0
    while i < len(arr) and j < len(dep):
        if arr[i] < dep[j]:
            count += 1
            i += 1
        else:
            count -= 1
            j += 1
        maxGuest = max(maxGuest, count)
    count += len(arr) - i
    return max(maxGuest, count)

print(meetingMaxGuests([1200,1100,1000,900,800,700,600,500],[840,820,830,530]))