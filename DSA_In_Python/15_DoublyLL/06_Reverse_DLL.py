from ListNode import ListNode

def reverse(head):
    if not head or not head.next:
        return head
    temp = head
    while temp.next:
        temp.next, temp.prev = temp.prev, temp.next
        temp = temp.prev
    temp.next, temp.prev = temp.prev, temp.next
    return temp

head = ListNode.create([10,20,30,40])
print(reverse(head))

head = ListNode.create([10])
print(reverse(head))

head = ListNode.create([])
print(reverse(head))