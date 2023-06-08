# Consider the first index value is sorted. And look from the 2nd index value and compare with the seroted part & swap the value in the right position

# Time : O(n^2) Space : O(1)
def insertionSort(nums):
    n = len(nums)
    for i in range(1, n):
        temp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > temp:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = temp
    return nums

print(insertionSort([20,5,40,60,10,30]))

# [20] [5,40,60,10,30]
# [5,20] [40,60,10,30]
# [5,20,40] [60,10,30]   
#       k = 4                   k = 3                   k = 2                           k = 1
# [5,20,40,60,10] [30] => t=10 [2,20,40,60,60] [30] => t=10 [2,20,40,40,60] [30] => t=10 [2,20,20,40,60] => [2,10,20,40,60] [30]