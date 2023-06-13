from TreeNode import TreeNode
from collections import deque

def maxWidthOfBinaryTree(root):
    if not root:
        return 0
    queue = deque([root])
    maxWidth = 1
    while queue:
        n = len(queue)
        maxWidth = max(maxWidth, n)
        for _ in range(n):
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    return maxWidth

root = TreeNode.create([10,20,30,40,None,50,60,80])
print(maxWidthOfBinaryTree(root))

root = TreeNode.create([10,20,30,40,50,60,70])
print(maxWidthOfBinaryTree(root))