from TreeNode import TreeNode

def inOrder_Iterative(root):
    st, res = [], []
    while st or root:
        if root:
            st.append(root)
            root = root.left
        else:
            root = st.pop()
            res.append(root.val)
            root = root.right
    return res

root = TreeNode.create([10,20,30,40,50,60])
print(inOrder_Iterative(root))