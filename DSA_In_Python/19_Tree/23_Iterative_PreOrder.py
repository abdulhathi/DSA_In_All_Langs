from TreeNode import TreeNode

def preOrder_Iterative(root):
    st, res = [], []
    while st or root:
        if root:
            res.append(root.val)
            st.append(root)
            root = root.left
        else:
            root = st.pop()
            root = root.right
    return res

root = TreeNode.create([10,20,30,40,50,60])
print(preOrder_Iterative(root))