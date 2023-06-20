class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        res = [-1] * n
        kRadLen = (2*k)+1
        # Sum up to k
        kRadLeftSum = 0
        for i in range(k):
            kRadLeftSum += nums[i]
        
        # Sum after k to k + k
        kRadRightSum = 0
        for i in range(k+1, kRadLen):
            kRadRightSum += nums[i]

        for i in range(n):
            if i-k < 0 or i+k >= n:
                continue
            if i-k > 0:
                kRadLeftSum -= nums[i-k-1]
                kRadLeftSum += nums[i-1]
                kRadRightSum -= nums[i]
                kRadRightSum += nums[i+k]
            res[i] = (kRadLeftSum + nums[i] + kRadRightSum) // kRadLen
        return res
    
print(Solution().getAverages([7,4,3,9,1,8,5,2,6], 3))



class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        if k == 0:
            return nums
        n = len(nums)
        res = []
        preSum = [nums[0]]
        kRadLen = (2*k) + 1

        for i in range(1, n):
            preSum.append(preSum[i-1] + nums[i])

        for i in range(n):
            if i-k < 0 or i+k >= n:
                res.append(-1)
            else:
                kRadSum = preSum[i-1] - (preSum[i-k-1] if i-k-1 >= 0 else 0)
                kRadSum += nums[i] + (preSum[i+k]-preSum[i])
                res.append(kRadSum // kRadLen)
        return res