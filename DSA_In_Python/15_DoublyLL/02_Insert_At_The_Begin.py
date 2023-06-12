from ListNode import ListNode

# Time : O(1) Space : O(1)
def insertAtBegin(head, key):
    node = ListNode(key)
    if not head:
        return node
    node.next, head.prev = head, node
    return node

head = ListNode.create([10,15,20])
print(insertAtBegin(head, 5))