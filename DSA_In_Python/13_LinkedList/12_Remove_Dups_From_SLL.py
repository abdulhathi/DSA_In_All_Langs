from ListNode import ListNode

# Time : O(n) Space : O(1)
def removeDups(head):
    if not head:
        return None
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

head = ListNode.create([10,20,20,20,30,30])
print(removeDups(head))

head = ListNode.create([5,10,15,20])
print(removeDups(head))