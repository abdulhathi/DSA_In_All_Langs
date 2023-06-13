from TreeNode import TreeNode

# Time : O(n) Space : O(h)
def convertBinaryTreeToDLL(root):
    head = None
    temp = None
    def convert(root):
        nonlocal temp, head
        if not root:
            return
        convert(root.left)
        if not head:
            head = root 
            temp = head
        else:
            temp.right = root
            root.left = temp
            temp = temp.right
        convert(root.right)
    convert(root)
    return head

root = TreeNode.create([10,5,20,None,None,30,35])
dll = convertBinaryTreeToDLL(root)
res = []
while dll:
    res.append(dll.val)
    dll = dll.right
print(res)