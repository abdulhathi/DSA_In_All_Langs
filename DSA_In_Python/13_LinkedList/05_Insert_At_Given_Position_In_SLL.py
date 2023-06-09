from ListNode import ListNode

# Time : O(pos)
def insertAtGivenPosition(head, pos, key):
    node = ListNode(key)
    if pos == 1:
        node.next = head
        return node
    temp = head
    i = 2
    while temp:
        if pos == i:
            node.next = temp.next
            temp.next = node 
            break
        temp = temp.next
        i += 1
    return head

head = ListNode.create([1,2,3])
print(insertAtGivenPosition(head, 1, 8))
head = ListNode.create([1,2,3])
print(insertAtGivenPosition(head, 2, 8))
head = ListNode.create([1,2,3])
print(insertAtGivenPosition(head, 4, 8))