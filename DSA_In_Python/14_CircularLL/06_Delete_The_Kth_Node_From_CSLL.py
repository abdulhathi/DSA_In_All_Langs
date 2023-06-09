from ListNode import ListNode

def deleteKthNode(head, k):
    if not head:
        return None
    if k == 1:
        head.val = head.next.val
        head.next = head.next.next
        return head
    temp = head
    for _ in range(k-2):
        temp = temp.next

    temp.next = temp.next.next
    return head

head = ListNode.create([1,2,3,4,5], True)
print(deleteKthNode(head, 3))

head = ListNode.create([1,2,3,4,5], True)
print(deleteKthNode(head, 1))

head = ListNode.create([1,2,3,4,5], True)
print(deleteKthNode(head, 2))

head = ListNode.create([1,2,3,4,5], True)
head = deleteKthNode(head, 5)
print(head.next.next.next.next.val)
