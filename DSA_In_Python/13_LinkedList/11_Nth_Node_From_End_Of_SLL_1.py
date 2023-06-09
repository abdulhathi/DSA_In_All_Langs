from ListNode import ListNode

# Time : O(n) Space : O(1)
def nthNodeFromEnd(head, n):
    temp = head
    for _ in range(n):
        if not temp:
            return None
        temp = temp.next
    first, second = temp, head
    while first:
        first = first.next
        second = second.next
    return second


head = ListNode.create([10,20,30,40,50])
print(nthNodeFromEnd(head, 2))

head = ListNode.create([10,20,30])
print(nthNodeFromEnd(head, 3))

head = ListNode.create([10,20,30])
print(nthNodeFromEnd(head, 1))

head = ListNode.create([10,20])
print(nthNodeFromEnd(head, 3))

