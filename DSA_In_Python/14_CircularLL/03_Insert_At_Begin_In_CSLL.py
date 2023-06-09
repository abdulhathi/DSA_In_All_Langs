from ListNode import ListNode

def insertAtBegin(head, key):
    node = ListNode(key)
    if not head:
        node.next = node
        return node
    node.next = head
    temp = head.next
    while temp.next != head:
        temp = temp.next
    
    temp.next = node
    return node

head = ListNode.create([2,3,4,5], True)
print(insertAtBegin(head, 1))

# Constant time change the key
def insertAtBegin(head, key):
    node = ListNode(key)
    if not head:
        node.next = node
        return node
    node.next, head.next = head.next, node
    head.val, node.val = node.val, head.val
    return head

head = ListNode.create([2,3,4,5], True)
print(insertAtBegin(head, 1))