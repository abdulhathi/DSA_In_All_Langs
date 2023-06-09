from ListNode import ListNode

# Time : O(n) Space : O(1)
def nthNodeFromEnd(head, n):
    temp, count = head, 0
    while temp:
        count += 1
        temp = temp.next
    pos = count - n
    if pos < 0:
        return None
    temp = head
    for _ in range(pos):
        temp = temp.next
    return temp

head = ListNode.create([10,20,30,40,50])
print(nthNodeFromEnd(head, 2))

head = ListNode.create([10,20,30])
print(nthNodeFromEnd(head, 3))

head = ListNode.create([10,20,30])
print(nthNodeFromEnd(head, 1))

head = ListNode.create([10,20])
print(nthNodeFromEnd(head, 3))