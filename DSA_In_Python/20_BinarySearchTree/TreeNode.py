from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    @staticmethod
    def create(nums):
        def createBST(root, key):
            if not root:
                return TreeNode(key)
            elif key > root.val:
                root.right = createBST(root.right, key)
            else:
                root.left = createBST(root.left, key)
            return root

        root = None
        for num in nums:
            root = createBST(root, num)
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