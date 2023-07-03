def partitionGivenArray(arr, ind):
    pivot = arr[ind]
    temp = []
    for num in arr:
        if num <= pivot:
            temp.append(num)
    
    for num in arr:
        if num > pivot:
            temp.append(num)
    
    return temp

print(partitionGivenArray([3,8,6,12,10,7],5))

print(partitionGivenArray([3,8,6,12,10,7],1))