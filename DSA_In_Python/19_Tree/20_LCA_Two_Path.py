from TreeNode import TreeNode
from collections import deque

# Time  : O(n) Space : O(h)
def twoPathLCA(root, node1, node2):
    path1, path2 = deque(), deque()
    
    def findPath(root, node, path):
        if not root:
            return False
        path.append(root.val)
        if root == node:
            return True
        left = findPath(root.left, node, path)
        if left:
            return True
        right = findPath(root.right, node, path)
        if right:
            return True
        path.pop()
        return False
    
    findPath(root, node1, path1)
    findPath(root, node2, path2)
    lca = -1
    while path1 and path2 and path1[0] == path2[0]:
        p1Val = path1.popleft()
        path2.popleft()
        lca = p1Val
    return lca
        
root = TreeNode.create([10,50,60,70,20,None,None,40,None,90,80,None,None,30])
print(twoPathLCA(root, root.left.right.left.left, root.left.right.right))