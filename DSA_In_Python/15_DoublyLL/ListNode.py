class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
    
    def __str__(self):
        if not self:
            return None
        res = []
        temp = self
        while temp:
            nextVal = str(temp.next.val) if temp.next else "N"
            prevVal = str(temp.prev.val) if temp.prev else "N"
            nodeVal = f"[{prevVal}<-{temp.val}->{nextVal}]"
            res.append(nodeVal)
            temp = temp.next
        return " ".join(res)
    
    @staticmethod
    def create(nums):
        if not nums:
            return None
        head = ListNode(nums[0])
        temp = head
        for i in range(1, len(nums)):
            temp.next = ListNode(nums[i], temp)
            temp = temp.next
        return head