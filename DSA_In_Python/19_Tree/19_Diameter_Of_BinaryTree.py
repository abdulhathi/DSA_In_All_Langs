from TreeNode import TreeNode

# Time : (n) Space : O(h)
def diameterOfBT(root):
    maxDiameter = 0
    def diameter(root):
        nonlocal maxDiameter
        if not root:
            return 0
        lh, rh = diameter(root.left), diameter(root.right)
        maxDiameter = max(lh + rh + 1, maxDiameter)
        return max(lh, rh) + 1
    diameter(root)
    return maxDiameter

root = TreeNode.create([10,20,30,None,None,40,50,60])
print(diameterOfBT(root))

root = TreeNode.create([10,20,60,30,80,None,None,50,40,None,90,60,None,None,None,18])
print(diameterOfBT(root))

root = TreeNode.create([10,20,None,30])
print(diameterOfBT(root))