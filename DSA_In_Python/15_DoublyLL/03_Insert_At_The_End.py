from ListNode import ListNode

def insertAtEnd(head, key):
    node = ListNode(key)
    if not head:
        return node
    temp = head
    while temp.next:
        temp = temp.next
    temp.next, node.prev = node, temp

    return head

head = ListNode.create([10,20,30])
print(insertAtEnd(head,40))