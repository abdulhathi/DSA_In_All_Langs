from ListNode import ListNode

def createDLL(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    temp = head
    for i in range(1, len(nums)):
        temp.next = ListNode(nums[i], temp)
        temp = temp.next
    return head

print(createDLL([1,2,3,4]))