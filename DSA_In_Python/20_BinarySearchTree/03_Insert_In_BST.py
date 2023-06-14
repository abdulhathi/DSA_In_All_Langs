from TreeNode import TreeNode

def insertInBST(root, key):
    if not root:
        return TreeNode(key)
    elif key > root.val:
        root.right = insertInBST(root.right, key)
    else:
        root.left = insertInBST(root.left, key)
    return root

root = TreeNode.create([10,5,15,12,18])
print(insertInBST(root, 20))
print(root.right.right.right)

"""
                (10)
        (5)             (15)
                    (12)    (18)
                                (20)
"""

# Time : O(n) Space : (1)
def insertInBST_Iterative(root, key):
    temp = root
    parent = None
    while temp:
        parent = temp
        if key < temp.val:
            temp = temp.left
        else:
            temp = temp.right
    
    if not parent:
        return TreeNode(key)
    elif key > parent.val:
        parent.right = TreeNode(key)
    else:
        parent.left = TreeNode(key)
    return root

root = TreeNode.create([10,5,15,12,18])
print(insertInBST_Iterative(root, 20))
print(root.right.right.right)
