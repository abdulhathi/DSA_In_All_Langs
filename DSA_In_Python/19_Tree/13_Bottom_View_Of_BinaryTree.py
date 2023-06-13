"""
COL -2      -1    0     1       2
                (10)
          (20)         (50)
    (30)        (40)          (70)
                (60)

O/P : 30, 20, 60, 50, 70
"""             
from TreeNode import TreeNode
from collections import deque, defaultdict

# Time : O(n) Space : O(n)
def bottomViewOfBinayTree(root):
    dic = defaultdict(int)
    queue = deque([(root, 0)])
    lp, rp = 0, 0
    while queue:
        n = len(queue)
        for _ in range(n):
            curr, col = queue.popleft()
            dic[col] = curr.val
            lp = min(lp, col)
            rp = max(rp, col)
            if curr.left:
                queue.append((curr.left, col-1))
            if curr.right:
                queue.append((curr.right, col+1))

    res = []
    for key in range(lp, rp+1):
        res.append(dic[key])
    return res

root = TreeNode.create([10,20,50,30,40,60,70])
print(bottomViewOfBinayTree(root))