from ListNode import ListNode

# Time : O(1) Space : O(1)
def insertAtBegining(head, key):
    return ListNode(key, head)

head = ListNode.create([])
print(insertAtBegining(head, 10))

head = ListNode.create([10,20,30])
print(insertAtBegining(head, 50))