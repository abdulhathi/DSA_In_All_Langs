def merge(nums, l, m, h):
	nums1, nums2 = nums[l: m+1], nums[m+1: h+1]
	i, j, k, m, n = 0, 0, l, len(nums1), len(nums2)
	
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
  
# Time : O(nlogn) Space : O(n)
def mergeSort(nums, l, r):
	if r > l:
		m = (l+r)//2
		mergeSort(nums, l, m)
		mergeSort(nums, m+1, r)
		merge(nums, l, m, r)
    
nums = [10,15,20,11,13]
mergeSort(nums, 0, 4)
print(nums)