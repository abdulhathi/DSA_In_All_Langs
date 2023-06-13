from TreeNode import TreeNode

def getSize(root):
    if not root:
        return 0
    leftSize = getSize(root.left)
    rightSize = getSize(root.right)
    return 1 + leftSize + rightSize

root = TreeNode.create([10,20,30,None,None,40,50])
print(getSize(root))