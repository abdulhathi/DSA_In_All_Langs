from ListNode import ListNode

class StackByDLL:
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0

    def push(self, key):
        node = ListNode(key, self.tail.prev, self.tail)
        node.prev.next, node.next.prev = node, node
        self._size += 1

    def pop(self):
        if self._size == 0:
            return None
        node = self.tail.prev
        node.prev.next, self.tail.prev = self.tail, node.prev
        self._size -= 1
        node.next, node.prev = None, None
        return node

    def peek(self):
        if self._size == 0:
            return None
        return self.tail.prev

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0
    
    def __str__(self):
        res = []
        if not self._size:
            return res
        temp = self.head.next
        while temp != self.tail:
            res.append(str(temp.val))
            temp = temp.next
        return ",".join(res)
    
st = StackByDLL()
# Push
st.push(10)
st.push(20)
st.push(30)
print(st)
print(st.size())

# Pop
print(st.pop())
print(st)

# Size
print(st.size())

# Peek
print(st.peek())


li = [[[0,0]] for _ in range(5)]
print(li)