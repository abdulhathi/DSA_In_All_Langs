# TIME : O(logN) SPACE : O(n)
def binarySearch(nums, target):
    lp, rp = 0, len(nums) - 1
    while lp <= rp:
        mid = (lp + rp) // 2
        if nums[mid] == target:
            return mid
        else:
            lp, rp = [lp, mid-1] if nums[mid] > target else [mid+1, rp]
    return -1

print(binarySearch([10,20,30,40,50,60], 20))
print(binarySearch([5,15,25], 25))
print(binarySearch([5,10,15,25,35], 20))
print(binarySearch([10,10], 10))