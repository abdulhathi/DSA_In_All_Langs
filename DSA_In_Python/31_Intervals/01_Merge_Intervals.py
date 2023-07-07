
# Time : O(nlogn)
def mergeIntervals(intervals):
    intervals.sort()
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        p = merged[len(merged)-1]
        c = intervals[i]
        if c[0] <= p[0] <= c[1] or p[0] <= c[0] <= p[1]:
            merged[len(merged)-1] = [min(p[0], c[0]), max(p[1], c[1])]
        else:
            merged.append(c)

    return merged

print(mergeIntervals([[1,3],[2,4],[5,7],[6,8]]))
print(mergeIntervals([[7,9],[6,10],[4,5],[1,3],[2,4]]))

