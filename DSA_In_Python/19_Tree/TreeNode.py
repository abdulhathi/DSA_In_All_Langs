from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def create(nums):
        if not nums:
            return None
        i, n = 0, len(nums)
        root = TreeNode(nums[i])
        i += 1
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if not curr:
                continue
            if i < n:
                curr.left = TreeNode(nums[i]) if nums[i] else nums[i]
                queue.append(curr.left)
                i += 1
            if i < n:
                curr.right = TreeNode(nums[i]) if nums[i] else nums[i]
                queue.append(curr.right)
                i += 1
        return root

    def __str__(self):
        res = []
        if not self:
            return res
        queue = deque([self])
        while queue:
            curr = queue.popleft()
            if not curr:
                continue
            res.append(str(curr.val))
            queue.append(curr.left)
            queue.append(curr.right)
        return " ".join(res)