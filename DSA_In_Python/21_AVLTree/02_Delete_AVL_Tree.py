from TreeNode import TreeNode

def LLRotation(root):
    temp = root.left.right
    root.left.right, root = root, root.left
    root.right.left = temp
    return root
    
def RRRotation(root):
    temp = root.right.left
    root.right.left, root = root, root.right
    root.left.right = temp
    return root
    
def LRRotation(root):
    left, right = root.left.right.left, root.left.right.right
    nextRoot = root.left.right
    nextRoot.left, nextRoot.right = root.left, root
    root = nextRoot
    root.left.right, root.right.left = left, right
    return root

def RLRotation(root):
    left, right = root.right.left.left, root.right.left.right
    nextRoot = root.right.left
    nextRoot.left, nextRoot.right = root, root.right
    root = nextRoot
    root.left.right, root.right.left = left, right
    return root
    
def getHeight(root):
    if not root:
        return 0
    return max(getHeight(root.left), getHeight(root.right)) + 1

def balanceFactor(root):
    return getHeight(root.left) - getHeight(root.right)

def inOrderSucc(root):
    while root.left:
        root = root.left
    return root

def deleteAVLTree(root, key):

    def delete(root, key):
        if not root:
            return None
        if key == root.val:
            if not root.left and not root.right:
                return None
            elif not root.right or not root.right:
                return root.left if root.left else root.right
            else:
                temp = inOrderSucc(root.right)
                root.val = temp.val
                root.right = delete(root.right, temp.val)
        elif key > root.val:
            root.right = delete(root.right, key)
        else:
            root.left = delete(root.left, key)
        
        rootBF = balanceFactor(root)
        if rootBF == 2:
            rootLeftBF = balanceFactor(root.left)
            if rootLeftBF == 1:
                root = LLRotation(root)
            else:
                root = LRRotation(root)
        elif rootBF == -2:
            rootRightBF = balanceFactor(root.right)
            if rootRightBF == -1:
                root = RRRotation(root)
            else:
                root = RLRotatioin(root)
        return root
    
    return delete(root, key)

root = TreeNode.create([20, 15, 40, 5, 18, 50])
root = deleteAVLTree(root, 50)
print(root)
root = deleteAVLTree(root, 40)
print(root)