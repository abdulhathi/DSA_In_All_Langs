from ListNode import ListNode

def deleteHead(head):
    if not head or not head.next:
        return None
    head = head.next
    head.prev = None
    return head

head = ListNode.create([10,20,30])
print(deleteHead(head))

head = ListNode.create([])
print(deleteHead(head))

head = ListNode.create([10])
print(deleteHead(head))