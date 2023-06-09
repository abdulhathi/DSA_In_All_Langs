class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        res = []
        temp = self
        while temp:
            res.append(str(temp.val))
            temp = temp.next
            if temp == self:
                break
        return ",".join(res)

    @staticmethod
    def create(nums, isCircular = False):
        if not nums:
            return None
        head = ListNode(nums[0])
        temp = head
        for i in range(1, len(nums)):
            temp.next = ListNode(nums[i])
            temp = temp.next
        if isCircular:
            temp.next = head
        return head