from TreeNode import TreeNode

# Time : O(n^2) Space : O(h)
def constructBSTFromInAndPreOrder(inOrdr, preOrdr):
    ind = 0
    def construct(inOrder, preOrder, lp, rp):
        nonlocal ind
        if lp > rp:
            return None
        if ind >= len(preOrder):
            return None
        root = TreeNode(preOrder[ind])
        ind += 1
        for i in range(lp, rp+1):
            if inOrder[i] != root.val:
                continue
            root.left = construct(inOrder, preOrder, lp, i-1)
            root.right = construct(inOrder, preOrder, i+1, rp)
            break
        return root
    
    return construct(inOrdr, preOrdr, 0, len(preOrdr)-1)

# root = constructBSTFromInAndPreOrder([20,10,30], [10,20,30])
# print(root)

root = constructBSTFromInAndPreOrder([40,20,50,10,30,80,70,90], [10,20,40,50,30,70,80,90])
print(root)

"""
                    10
            20              30
        40      50              70
                            80      90
"""