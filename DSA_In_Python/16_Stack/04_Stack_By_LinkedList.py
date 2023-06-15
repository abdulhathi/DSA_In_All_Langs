from ListNode import ListNode

class StackByLL:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, val):
        node = ListNode(val, self.head)
        self.head = node
        self.size += 1

    def pop(self):
        if not self.head:
            return
        node = self.head
        self.head = self.head.next
        self.size -= 1
        return node.val

    def peek(self):
        if self.head:
            return self.head.val

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0
        