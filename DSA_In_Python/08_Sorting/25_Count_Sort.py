
# Time : O(maxVal+1) Space : O(maxVal+1)
def countSort(arr):
    maxVal = max(arr)
    count = [0] * (maxVal+1)
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    for num in reversed(arr):
        count[num] -= 1
        output[count[num]] = num
    
    return output


print(countSort([1,4,4,1,0,1]))