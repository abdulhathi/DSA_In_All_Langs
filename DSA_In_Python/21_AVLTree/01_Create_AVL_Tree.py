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

def createAVLTree(nums):

    def create(root, key):
        if not root:
            return TreeNode(key)
        elif key > root.val:
            root.right = create(root.right, key)
        else:
            root.left = create(root.left, key)

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
                root = RLRotation(root)
        return root

    root = None
    for num in nums:
        root = create(root, num)
    return root

root = createAVLTree([20,15,5,40,50,18])
print(root)