from typing import Optional
from TreeNode import TreeNode

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        st = []
        pathSum = 0
        while st or root:
            if root:
                pathSum += root.val
                st.append(root)
                root = root.left
            else:
                root = st.pop()
                if not root.left and not root.right:
                    if pathSum == targetSum:
                        return True
                    else:
                        pathSum -= root.val
                root = root.right
        return False
    
root = TreeNode.create([1,-2,-3,1,3,-2,None,-1])
print(Solution().hasPathSum(root, 3))