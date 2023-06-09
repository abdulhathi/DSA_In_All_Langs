from ListNode import ListNode

# Time : O(1) Space : O(1)
def deleteFirstNode(head):
    if not head:
        return None
    return head.next

head = ListNode.create([])
print(deleteFirstNode(head))

head = ListNode.create([1,2,3,4])
print(deleteFirstNode(head))