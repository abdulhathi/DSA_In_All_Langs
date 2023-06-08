# Time : O(m+n) Space : O(m+n)
def mergeSubarrays(nums, low, mid, high):
	nums1, nums2 = nums[low: mid+1], nums[mid+1: high+1]
	i, j, k, m, n = 0, 0, 0, len(nums1), len(nums2)
	while i < m and j < n:
		if nums1[i] <= nums2[j]:
			nums[k] = nums1[i]
			i += 1
		else:
			nums[k] = nums2[j]
			j += 1
		k += 1
	
	while i < m:
		nums[k] = nums1[i]
		i += 1
		k += 1
	
	while j < n:
		nums[k] = nums2[j]
		j += 1
		k += 1
	
	return nums


print(mergeSubarrays([10,15,20,11,13], 0, 2, 4))
print(mergeSubarrays([5,8,12,14,7],0,3,4))