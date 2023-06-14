from TreeNode import TreeNode

# Time : O(logn) space : O(1)
def searchBST(root, key):
    while root:
        if root.val == key:
            return True
        elif key > root.val:
            root = root.right
        else:
            root = root.left
    return False

root = TreeNode.create([20,10,40,5,30,80,50,100])
print(searchBST(root, 50))

root = TreeNode.create([20,10,40,5,30,80,50,100])
print(searchBST(root, 200))