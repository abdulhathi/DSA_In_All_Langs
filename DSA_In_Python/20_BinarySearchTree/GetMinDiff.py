from TreeNode import TreeNode
from collections import deque
import math

def getMinimumDifference(root) -> int:
    pair = deque()
    minDiff = math.inf
    def inOrder(root):
        nonlocal minDiff
        if not root:
            return
        inOrder(root.left)
        pair.append(root.val)
        if len([pair]) > 1:
            minDiff = min(abs(pair[0] - pair[1]), minDiff)
            pair.popleft()
        inOrder(root.right)
    inOrder(root)
    return minDiff

root = TreeNode.create([4,2,6,1,3])
print(getMinimumDifference(root))