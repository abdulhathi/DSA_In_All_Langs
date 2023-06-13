from TreeNode import TreeNode
res = []
def postOrder_Recursive(root):
    # 👈
    if not root:
        return
    postOrder_Recursive(root.left)
    postOrder_Recursive(root.right)
    res.append(root.val)

root = TreeNode.create([1,2,3,4,5,6,7])
postOrder_Recursive(root)
print(res)