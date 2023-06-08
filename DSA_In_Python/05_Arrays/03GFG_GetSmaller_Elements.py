def getSmallerElements(nums, x):
	res = []
	for num in nums:
		if num < x:
			res.append(num)
	return res

print(getSmallerElements([8, 100, 20, 40, 3, 7], 10))
print(getSmallerElements([100, 20, 40, 60, 80, 200], 60))

# Get Smaller elements using list complrehension method

def getSmallerElements(nums, x):
	res = [num for num in nums if num < x]
	return res

print(getSmallerElements([8, 100, 20, 40, 3, 7], 10))
print(getSmallerElements([100, 20, 40, 60, 80, 200], 60))