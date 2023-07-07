
# Hoores partition Time : O(n)
def partitionArroundRange(arr, rangeVal):
    lp, mp, rp = 0, 0, len(arr)-1
    while mp <= rp:
        if arr[mp] < rangeVal[0]:
            arr[lp], arr[mp] = arr[mp], arr[lp]
            lp, mp = lp+1, mp+1
        elif rangeVal[0] <= arr[mp] <= rangeVal[1]:
            mp += 1
        else:
            arr[mp], arr[rp] = arr[rp], arr[mp]
            rp -= 1
    
    return arr

print(partitionArroundRange([10,5,6,3,20,9,40,4], [5,10]))


# for i in range(32):
#     print(((1 >> i) & 1), end=",")
# print()

num = 1
print(bin(num >> 31))
print(1 + (num >> 31) - (-num >> 31))