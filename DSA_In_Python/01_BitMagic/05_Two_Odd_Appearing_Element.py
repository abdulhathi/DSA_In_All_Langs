
# Time : O(n) Space : O(1)
def twoOddAppearingElement(arr):
    # XOR of all the elements will finally will give the two odd element and its XOR value
    # 5,6,10,6,10,6,3,3     => 5^6 => 3 (0011)

    res = arr[0]
    for i in range(1, len(arr)):
        res = res ^ arr[i]
    

    # Find the least set bit elements in the array and XOR of all to get the first odd appear element
    # And least set bit is zero elements XOR of all will give the second odd appear element

    # print(res & (~(res-1)))

    leastSetBit = 1
    while res & leastSetBit == 0:
        leastSetBit <<= 1

    res1, res2 = 0, 0
    for num in arr:
        if num & leastSetBit > 0:
            res1 = res1 ^ num
        else:
            res2 = res2 ^ num

    return res1, res2


print(twoOddAppearingElement([5,6,10,6,10,6,3,3]))