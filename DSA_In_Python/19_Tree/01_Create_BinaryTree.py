from TreeNode import TreeNode
from collections import deque

def createBinaryTree(nums):
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
            curr.left = TreeNode(nums[i])
            queue.append(curr.left)
            i += 1
        if i < n:
            curr.right = TreeNode(nums[i])
            queue.append(curr.right)
            i += 1
    return root

print(createBinaryTree([1,2,3,4,5,6,7]))


