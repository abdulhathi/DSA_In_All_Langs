from ListNode import ListNode

# Time : O(n) Space : O(1)
def searchSLL(head, key):
    i = 1
    while head:
        if head.val == key:
            return i
        i += 1
        head = head.next
    return -1

head = ListNode.create([1,2,3,4])
print(searchSLL(head, 3))
print(searchSLL(ListNode.create([10,50]), 20))
