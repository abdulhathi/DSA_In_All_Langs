from TreeNode import TreeNode

def getHeight(root):
    if not root:
        return 0
    leftHeight = getHeight(root.left)
    rightHeight = getHeight(root.right)
    return max(leftHeight, rightHeight) + 1

root = TreeNode.create([1,2,3,4,5,6,7])
print(getHeight(root))

root = TreeNode.create([10,8,30,None,None,40,50,None,None,70])
print(getHeight(root))

root = TreeNode.create([10])
print(getHeight(root))

root = TreeNode.create([10,20,None,30])
print(getHeight(root))

root = TreeNode.create([])
print(getHeight(root))