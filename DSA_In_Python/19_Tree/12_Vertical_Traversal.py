from TreeNode import TreeNode
from collections import deque, defaultdict;

# Time : O(n) Space : O(n)
def verticalTraversal(root):
    dic = defaultdict(list)
    queue = deque([(root, 0)])
    lp, rp = 0, 0
    while queue:
        n = len(queue)
        for _ in range(n):
            curr, col = queue.popleft()
            lp = min(lp, col)
            rp = max(rp, col)
            dic[col].append(curr.val)
            if curr.left:
                queue.append((curr.left, col-1))
            if curr.right:
                queue.append((curr.right, col+1))
    
    res = []
    for key in range(lp, rp+1):
        res.append(dic[key])
    return res

root = TreeNode.create([10,20,30,None,None,40,50])
print(verticalTraversal(root))