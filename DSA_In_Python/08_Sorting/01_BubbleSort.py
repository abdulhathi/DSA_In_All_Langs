# Time : O(n^2) Space : O(1)
# In every pass we need check the value with its prev value. If the prev Value is greater we need to swap.
# If there is no swap in a pass. Then the array is sorted we can exit from the loop and return the value.
def bubbleSort(nums):
    n = len(nums)
    for i in range(n-1):
        swapped = False
        for j in range(1, n-i):
            if nums[j-1] <= nums[j]:
                continue
            nums[j-1], nums[j] = nums[j], nums[j-1]
            swapped = True
        if not swapped:
            break
    return nums
        
print(bubbleSort([2,10,8,7]))