# TIME : O(n) SPACE : O(1)

def largestElement(nums):
	largest = nums[0]
	for i in range(1, len(nums)):
		largest = nums[i] if nums[i] > largest else largest
	return largest

print(largestElement([10, 5, 20, 8]))
print(largestElement([30, 30, 20]))
print(largestElement([40]))
