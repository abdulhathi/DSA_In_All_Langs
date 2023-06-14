from TreeNode import TreeNode

# Time : O(h) Space : O(1)
def ceilingInBST(root, key):
    res = None
    while root:
        if root.val == key:
            return key
        elif key > root.val:
            root = root.right
        else:
            res = root.val
            root = root.left
    return res

root = TreeNode.create([10,5,15,12,30])
print(ceilingInBST(root, 14))
print(ceilingInBST(root, 3))
print(ceilingInBST(root, 40))