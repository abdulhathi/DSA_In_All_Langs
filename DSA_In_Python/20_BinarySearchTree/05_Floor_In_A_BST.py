from TreeNode import TreeNode

# Time : O(h) Space : O(1)
def floorInBST(root, key):
    res = None
    while root:
        if root.val == key:
            return key
        elif key > root.val:
            res = root.val
            root = root.right
        else:
            root = root.left
    return res

root = TreeNode.create([10,5,15,12,30])
print(floorInBST(root, 14))
print(floorInBST(root, 100))
print(floorInBST(root, 30))
print(floorInBST(root, 4))