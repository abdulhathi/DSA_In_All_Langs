from TreeNode import TreeNode
from collections import deque

def lineByLine_LevelOrder_Traversal(root):
    queue = deque([root])
    res = []
    while queue:
        line = []
        n = len(queue)
        for _ in range(n):
            curr = queue.pop()
            line.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        if line:
            res.append(line)
    return res

root = TreeNode.create([10,20,30,40,50,None,60,None,None,None,None,70,80])
res = lineByLine_LevelOrder_Traversal(root)
for line in res:
    print(line)

root = TreeNode.create([10,None,8,None,6])
res = lineByLine_LevelOrder_Traversal(root)
for line in res:
    print(line)
