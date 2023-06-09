from ListNode import ListNode

# Time : O(n) Space : O(1)
def deleteLastNode(head):
    if not head or not head.next:
        return None
    temp = head
    while temp.next.next:
        temp = temp.next
    temp.next = None
    return head

head = ListNode.create([1,2,3,4])
print(deleteLastNode(head))

print(deleteLastNode(ListNode.create([])))
print(deleteLastNode(ListNode.create([1])))