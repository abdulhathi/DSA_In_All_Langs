from TreeNode import TreeNode
from collections import deque

def levelOrder(root):
    res = []
    queue = deque([root])
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res

root = TreeNode.create([10,20,30,40,50,None,60,None,None,70,80])
print(levelOrder(root))
