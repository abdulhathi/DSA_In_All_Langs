from ListNode import ListNode

def deleteGivenPointerNode(node):
    if node.next:
        node.val = node.next.val
        node.next = node.next.next

head = ListNode.create([10,20,30,40,50])
deleteGivenPointerNode(head.next.next)
print(head)

head = ListNode.create([10,20,30,40,50])
deleteGivenPointerNode(head)
print(head)

head = ListNode.create([10])
deleteGivenPointerNode(head)
print(head)