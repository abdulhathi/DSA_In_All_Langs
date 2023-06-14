from TreeNode import TreeNode

# Time : O(h) Space : O(h)
def deleteInBST(root, key):
    def inOrderSucc(temp):
        while temp.left:
            temp = temp.left
        return temp
    
    def delete(root, key):
        if not root:
            return None
        if root.val == key:
            if not root.left and not root.right:
                return None
            elif not root.left or not root.right:
                return root.left if root.left else root.right
            else:
                temp = inOrderSucc(root.right)
                root.val = temp.val
                root.right = delete(root.right, temp.val)

        elif key > root.val:
            root.right = delete(root.right, key)
        else:
            root.left = delete(root.left, key)
        return root
    
    return delete(root, key)

root = TreeNode.create([40,20,100,30,70,200,60])
root = deleteInBST(root, 200)  # Leaf node
print(root)

root = deleteInBST(root, 20)  # Leaf node
print(root)

root = deleteInBST(root, 40)  # Leaf node
print(root)