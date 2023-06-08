# Time : O(m+n) Space : O(m+n)
def mergeTwoSortedList(nums1, nums2):
    res = []
    i, j, m, n = 0, 0, len(nums1), len(nums2)
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1

    while i < m:
        res.append(nums1[i])
        i += 1
    while j < n:
        res.append(nums2[j])
        j += 1

    return res

print(mergeTwoSortedList([10,15,20], [5,6,6,30]))
print(mergeTwoSortedList([1,1,2], [3]))