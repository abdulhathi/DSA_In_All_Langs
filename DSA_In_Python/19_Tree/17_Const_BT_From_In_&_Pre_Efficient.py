from TreeNode import TreeNode

def constBTFromInAndPre_Efficient(inOrdr, preOrdr):
    inOrdrDic = {val:ind for ind,val in enumerate(inOrdr)}
    ind = 0
    def construct(preOrder, lp, rp):
        nonlocal ind
        if lp > rp:
            return None
        if ind >= len(preOrder):
            return None
        root = TreeNode(preOrder[ind])
        ind += 1
        i = inOrdrDic[root.val]
        root.left = construct(preOrder, lp, i-1)
        root.right = construct(preOrder, i+1, rp)
        return root
    
    return construct(preOrdr, 0, len(preOrdr)-1)

root = constBTFromInAndPre_Efficient([20,10,30], [10,20,30])
print(root)

root = constBTFromInAndPre_Efficient([40,20,50,10,30,80,70,90], [10,20,40,50,30,70,80,90])
print(root)
