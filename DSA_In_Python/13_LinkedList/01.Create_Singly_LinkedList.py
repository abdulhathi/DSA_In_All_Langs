from ListNode import ListNode

# Time : O(n) Space : O(1)
def createSinglyLL(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    temp = head
    for i in range(1, len(nums)):
        temp.next = ListNode(nums[i])
        temp = temp.next
    return head

print(createSinglyLL([1,2,3,4,5]))
print(createSinglyLL([]))