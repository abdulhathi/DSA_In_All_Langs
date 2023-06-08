def leftRotate(nums):
  # Reverse list 0 to 1
	lp, rp = 0, 0
	while lp < rp:
		nums[lp], nums[rp] = nums[rp], nums[lp]
		lp, rp = lp+1, rp-1
	
	# Reverse list 1 to n
	lp, rp = 1, len(nums)-1
	while lp < rp:
		nums[lp], nums[rp] = nums[rp], nums[lp]
		lp, rp = lp+1, rp-1

	# Reverse the whole list
	lp, rp = 0, len(nums)-1
	while lp < rp:
		nums[lp], nums[rp] = nums[rp], nums[lp]
		lp, rp = lp+1, rp-1	

	return nums

print(leftRotate([10,20,30,40]))
print(leftRotate([1,2,3]))