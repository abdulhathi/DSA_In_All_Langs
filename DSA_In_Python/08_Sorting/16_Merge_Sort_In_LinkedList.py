from ListNode import ListNode

def divide(head):
    if not head or not head.next:
        return head, None
    if not head.next.next:
        left, right = head, head.next
        head.next = None
        return left, right
    
    slow, fast= head, head
    # slow, fast = head.next, head.next.next
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    left, right = head, slow.next
    slow.next = None
    return left, right

def mergeSortInLinkedList(head):
    def merge(left, right):
        dummy = ListNode(0)
        temp = dummy
        while left and right:
            if left.val <= right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        temp.next = left if left else right
        return dummy.next

    def divideList(head):
        if not head or not head.next:
            return head
        left, right = divide(head)
        left = divideList(left)
        right = divideList(right)
        return merge(left, right)
    
    return divideList(head)
    

head = ListNode.create([4,2,1,3])
print(mergeSortInLinkedList(head))

    
    

