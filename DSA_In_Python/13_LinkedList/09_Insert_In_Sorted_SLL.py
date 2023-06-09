from ListNode import ListNode

# Time : O(n) Space : O(1)
def insertInSortedSLL(head, key):
    node = ListNode(key)
    if not head:
        return node
    if key < head.val:
        node.next = head
        return node
    prev, curr = head, head.next
    while curr and curr.val < key:
        prev, curr = curr, curr.next
    node.next = prev.next
    prev.next = node
    return head

head = ListNode.create([10,20,30,40])
print(insertInSortedSLL(head, 25))

head = ListNode.create([10,25])
print(insertInSortedSLL(head, 5))

head = ListNode.create([10,20])
print(insertInSortedSLL(head, 30))

head = ListNode.create([])
print(insertInSortedSLL(head, 10))