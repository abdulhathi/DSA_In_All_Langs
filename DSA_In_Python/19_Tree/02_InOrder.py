from TreeNode import TreeNode

res = []
def inOrder_Recursive(root):
    # 👆
    if not root:
        return
    inOrder_Recursive(root.left)
    res.append(root.val)
    inOrder_Recursive(root.right)

root = TreeNode.create([1,2,3,4,5,6,7])     # 4,2,5,1,6,3,7
inOrder_Recursive(root) 
print(res)

"""
            (1)
    (2)             (3)
(4)     (5)     (6)     (7) 
"""

def inOrder_Iterative(root):
    # 👆
    pass