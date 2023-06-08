# Time : O(nlogn) Space : O(n)
def findIntervention(nums):
    iv = []
    count = 0
    def merge(li, l, mid, r):
        nonlocal count
        li1, li2 = li[l: mid+1], li[mid+1: r+1]
        i, j, k, m, n = 0, 0, l, len(li1), len(li2)
        while i < m and j < n:
            if li1[i] <= li2[j]:
                li[k] = li1[i]
                i += 1
            else:
                count += m - i
                for num in li1[i:]:
                    iv.append((num, li2[j]))
                li[k] = li2[j]
                j += 1
            k += 1
        while i < m:
            li[k] = li1[i]
            i, k = i+1, k+1
        while j < n:
            li[k] = li2[j]
            j, k = j+1, k+1

    def mergeSort(nums, l, r):
        if r > l:
            m = (r+l) // 2
            mergeSort(nums, l, m)
            mergeSort(nums, m+1, r)
            merge(nums, l, m, r)

    mergeSort(nums, 0, len(nums)-1)
    return iv, count

print(findIntervention([2,4,1,3,5]))
print(findIntervention([10,20,30,40]))
print(findIntervention([40,30,20,10]))
