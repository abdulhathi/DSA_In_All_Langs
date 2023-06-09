class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count = 0
        np = 0
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                nums[i] = None
                count += 1
                continue
            for j in range(np, i+1):
                np = j
                if nums[j] == None:
                    nums[j], nums[i] = nums[i], None
                    break
        return len(nums) - count
    
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))