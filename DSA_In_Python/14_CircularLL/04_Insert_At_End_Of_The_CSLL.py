from ListNode import ListNode

def insertAtEnd(head, key):
    node = ListNode(key)
    if not head:
        node.next = node
        return node
    tail = head.next
    while tail.next != head:
        tail = tail.next
    node.next, tail.next = head, node
    return head

head = ListNode.create([1,2,3,4], True)
print(insertAtEnd(head, 5))
print(head.next.next.next.next.val)

# Constant time
def insertAtEnd(head, key):
    node = ListNode(key)
    if not head:
        node.next = node
        return node
    node.next, head.next = head.next, node
    head.val, node.val = node.val, head.val
    return node

head = ListNode.create([1,2,3,4], True)
head = insertAtEnd(head, 5)
print(head)
print(head.next.next.next.next.val)