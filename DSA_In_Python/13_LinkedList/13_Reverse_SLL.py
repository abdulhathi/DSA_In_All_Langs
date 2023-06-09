from ListNode import ListNode

# Time : O(n) Space : O(1)
def reverse(head):
    prev, curr = None, head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

head = ListNode.create([10,20,30])
print(reverse(head))

head = ListNode.create([])
print(reverse(head))

head = ListNode.create([10])
print(reverse(head))