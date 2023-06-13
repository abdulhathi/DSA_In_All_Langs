from TreeNode import TreeNode

# Time : O(n) Space : O(h)
def LCA(root, node1, node2):
    if not root:
        return None
    if root == node1 or root == node2:
        return root
    left = LCA(root.left, node1, node2)
    right = LCA(root.right, node1, node2)
    if left and right:
        return root
    return left if left else right

root = TreeNode.create([10,50,60,70,20,None,None,40,None,90,80,None,None,30])
print(LCA(root, root.left.right.left.left, root.left.right.right))
