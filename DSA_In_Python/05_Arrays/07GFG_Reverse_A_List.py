def reverse(nums):
  lp, rp = 0, len(nums)-1
  while lp < rp:
    nums[lp], nums[rp] = nums[rp], nums[lp]
    lp, rp = lp+1, rp-1
  return nums

print(reverse([10,20,30,40]))
print(reverse(["geeks","ide","courses"]))