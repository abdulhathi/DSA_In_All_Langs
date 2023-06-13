from TreeNode import TreeNode

# Time : O(n) Space : O(k)
res = []
def printNodeAtDistK(root, k):
    if not root:
        return
    if k == 0:
        res.append(root.val)
    else:
        printNodeAtDistK(root.left, k-1)
        printNodeAtDistK(root.right, k-1)

root, k = TreeNode.create([10,20,30,40,50,None,70,None,None,None,None,None,80]), 2
printNodeAtDistK(root, k)
print(res)