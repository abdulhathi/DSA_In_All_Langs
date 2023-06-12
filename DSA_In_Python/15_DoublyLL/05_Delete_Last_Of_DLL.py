from ListNode import ListNode

# Time : O(n) Space : O(1)
def deleteLast(head):
    if not head or not head.next:
        return None
    temp = head
    while temp.next:
        temp = temp.next
    last = temp.prev
    last.next = None
    return head

head = ListNode.create([1,2,3,4])
print(deleteLast(head))

head = ListNode.create([1])
print(deleteLast(head))

