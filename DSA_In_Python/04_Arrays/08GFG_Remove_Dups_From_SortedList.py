def removeDuplicate(nums):
  lp, rp = 0, 1
  while rp < len(nums):
    if nums[lp] == nums[rp]:
      nums[rp] = None
      rp += 1
    elif nums[lp] < nums[rp]:
      val = nums[rp]
      nums[rp] = None
      nums[lp+1] = val
      lp, rp = lp+1, rp+1
  return nums

print(removeDuplicate([10,20,20,30,30,30,30]))
print(removeDuplicate([10,10,10]))