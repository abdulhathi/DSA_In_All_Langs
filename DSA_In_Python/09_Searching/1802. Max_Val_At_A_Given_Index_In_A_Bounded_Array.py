class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def calcSum(m, s, l):
            k = abs(m-l)
            if m > l:
                return s - (k*(k+1))//2
            elif m < l:
                return s + k
            else:
                return s

        lp, rp = 1, maxSum
        ll, rl = index, n - index - 1
        res = 1
        while lp <= rp:
            mid = (lp + rp) // 2
            m = mid - 1
            ls = rs = (m*(m+1))//2
            # left sum calculation
            ls = calcSum(m, ls, ll)
            rs = calcSum(m, rs, rl)
            ms = ls + mid + rs
            if ms <= maxSum:
                res = max(res, mid)
                lp = mid+1
            else:
                rp = mid-1
        return res
    
print(Solution().maxValue(6, 1, 10))