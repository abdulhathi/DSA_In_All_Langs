from ListNode import ListNode

# Time : O(n) Space : O(1)
def middleNodeOfSLL(head):
    count = 0
    temp = head
    while temp:
        count += 1
        temp = temp.next
    mid = count // 2
    temp = head
    while mid > 0:
        temp = temp.next
        mid -= 1
    return temp

head = ListNode.create([10,5,20,15,25])
print(middleNodeOfSLL(head))

head = ListNode.create([10,5,20,15,25,30])
print(middleNodeOfSLL(head))

head = ListNode.create([10])
print(middleNodeOfSLL(head))

head = ListNode.create([10,20])
print(middleNodeOfSLL(head))

head = ListNode.create([])
print(middleNodeOfSLL(head))


def middelOfTheSLL(head):
    if not head:
        return head
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

head = ListNode.create([10,5,20,15,25])
print(middelOfTheSLL(head))

head = ListNode.create([10,5,20,15,25,30])
print(middelOfTheSLL(head))

head = ListNode.create([10])
print(middelOfTheSLL(head))

head = ListNode.create([10,20])
print(middelOfTheSLL(head))

head = ListNode.create([])
print(middelOfTheSLL(head))