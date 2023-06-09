from ListNode import ListNode

# Time : O(n) Aux Space : O(1)
def reverseRecursive(head):
    def reverse(prev, curr):
        if not curr:
            return prev
        next = curr.next
        curr.next = prev
        return reverse(curr, next)
    
    return reverse(None, head)

head = ListNode.create([10,20,30])
print(reverseRecursive(head))

head = ListNode.create([])
print(reverseRecursive(head))

head = ListNode.create([10])
print(reverseRecursive(head))