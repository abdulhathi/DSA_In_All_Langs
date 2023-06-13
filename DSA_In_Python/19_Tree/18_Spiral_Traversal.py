from TreeNode import TreeNode
from collections import deque

# Time : O(n) Space : O(len(maxLevel))
def spiralTraversal(root):
    st1, st2 = [root], []
    res = []
    while st1 or st2:
        while st1:
            node = st1.pop()
            res.append(node.val)
            if node.left:
                st2.append(node.left)
            if node.right:
                st2.append(node.right)
        while st2:
            node = st2.pop()
            res.append(node.val)
            if node.right:
                st1.append(node.right)
            if node.left:
                st1.append(node.left)
    return res


root = TreeNode.create([1,2,3,4,5,6,7,8,9,None,None,10])
print(spiralTraversal(root))