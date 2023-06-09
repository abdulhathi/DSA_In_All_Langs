from ListNode import ListNode

# Time : O(n) Space : (1)
def traverseCSLL(head):
    res = []
    if not head:
        return res
    res.append(head.val)
    temp = head.next
    while temp and temp != head:
        res.append(temp.val)
        temp = temp.next
    return res

head = ListNode.create([1,2,3,4,5], True)
print(traverseCSLL(head))