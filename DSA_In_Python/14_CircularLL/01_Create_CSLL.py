from ListNode import ListNode

def createCSLL(nums):
    head = ListNode(nums[0])
    temp = head
    for i in range(1, len(nums)):
        temp.next = ListNode(nums[i])
        temp = temp.next
    temp.next = head
    return head

print(createCSLL([1,2,3,4]))
print(createCSLL([1]))