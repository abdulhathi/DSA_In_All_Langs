# PYTHON - TIME : O(n) - SPACE : O(1)
def isSorted(nums):
	for i in range(1, len(nums)):
		if nums[i-1] > nums[i]:
			return False
	return True

print(isSorted([10,20,30]))
print(isSorted([10,20,20,30]))
print(isSorted([10,5,2]))

# Check is sorted using Sorted method
# TIME : O(nlogn) SPACE : O(n)
def isSorted(nums):
	return sorted(nums) == nums

print(isSorted([10,20,30]))
print(isSorted([10,20,20,30]))
print(isSorted([10,5,2]))