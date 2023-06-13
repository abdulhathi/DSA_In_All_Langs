from TreeNode import TreeNode

def checkBalance(root):
    def isBalanced(root):
        if not root:
            return [0, True]
        leftHeight, leftBalance = isBalanced(root.left)
        if not leftBalance:
            return [0, False]
        rightHeight, rightBalance = isBalanced(root.right)
        if not rightBalance:
            return [0, False]
        if abs(leftHeight - rightHeight) > 1:
            return [0, False]
        return [max(leftHeight, rightHeight)+1, True]
    
    _, balance = isBalanced(root)
    return balance

root = TreeNode.create([18,4,20,None,None,13,70])
print(checkBalance(root))

root = TreeNode.create([3,4,8,5,9,None,7,None,None,None,None,6])
print(checkBalance(root))