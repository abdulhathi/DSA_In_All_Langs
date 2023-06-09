from ListNode import ListNode

# Constant time
def deleteTheHead(head):
    if not head or head.next == head:
        return None
    head.val = head.next.val
    head.next = head.next.next
    return head
    
head = ListNode.create([1,2,3,4], True)
print(head.next.next.next.next.val)
print(deleteTheHead(head))
print(head.next.next.next.val)