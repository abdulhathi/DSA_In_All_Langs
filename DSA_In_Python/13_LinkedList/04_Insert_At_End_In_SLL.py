from ListNode import ListNode

# Time : O(n) Space : O(1)
def insertAtEnd(head, key):
    node = ListNode(key)
    if not head:
        return node
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = node
    return head

head = ListNode.create([1,2,3,4])
print(insertAtEnd(head, 5))

head = None
print(insertAtEnd(head, 5))
