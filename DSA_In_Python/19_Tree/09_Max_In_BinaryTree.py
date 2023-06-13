from TreeNode import TreeNode
import math
 
def maxInBinaryTree(root):
    if not root:
        return -math.inf
    leftMax = maxInBinaryTree(root.left)
    rightMax = maxInBinaryTree(root.right)
    return max(root.val, leftMax, rightMax)
    
root = TreeNode.create([10,30,5,90,None,80,70])
print(maxInBinaryTree(root))

root = TreeNode.create([10,20,None,None,5])
print(maxInBinaryTree(root))

root = TreeNode.create([])
print(maxInBinaryTree(root))
