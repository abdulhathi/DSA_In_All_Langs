# Time : O(m+n) Space : O(m+n)
def intersectionOfTwoSortedList(l1, l2):
    i, j, m, n = 0, 0, len(l1), len(l2)
    res = []
    while i < m and j < n:
        if i > 0 and l1[i] == l1[i-1]:
            i += 1
            continue
        if l1[i] < l2[j]:
            i += 1
        elif l2[j] < l1[i]:
            j += 1
        elif l1[i] == l2[j]:
            res.append(l1[i])
            i, j = i+1, j+1

    return res

l1 = [3,5,10,10,10,15,15,20,50,50,50]
l2 = [5,10,10,15,30,30,30,30]

print(intersectionOfTwoSortedList(l1, l2))