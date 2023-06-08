# Time : O(m+n) Space : O(m+n)
def unionOfTwoSortedList(nums1, nums2):
	i, j, m, n = 0, 0, len(nums1), len(nums2)
	res = []
	while i < m and j < n:
		if nums1[i] == nums2[j]:
			i += 1
			continue
		if nums1[i] < nums2[j]:
			res.append(nums1[i])
			i += 1
		else:
			res.append(nums2[j])
			j += 1
	while i < m:
		if i > 0 and nums1[i] == nums1[i-1]:
			i += 1
			continue
		res.append(nums1[i])
		i += 1
	while j < n:
		if j > 0 and nums2[j] == nums2[j-1]:
			j += 1
			continue
		res.append(nums2[j])
		j += 1
  
	return res
  
print(unionOfTwoSortedList([3,5,8], [2,8,9,10,15]))
print(unionOfTwoSortedList([2,3,3,3], [3,4,4,4,4]))