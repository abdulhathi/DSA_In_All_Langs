from TreeNode import TreeNode

res = []
def preOrder_Recursive(root):
    # 👉 right 
    if not root:
        return
    res.append(root.val)
    preOrder_Recursive(root.left)
    preOrder_Recursive(root.right)

root = TreeNode.create([1,2,3,4,5,6,7])
preOrder_Recursive(root)
print(res)