from ListNode import ListNode

class MyDeque:
    def __init__(self):
        self._size = 0
        self.front = ListNode(0)
        self.rear = ListNode(0)
        self.front.next, self.rear.prev = self.rear, self.front

    def insertFront(self, key):
        node = ListNode(key, self.front, self.front.next)
        self.front.next.prev, self.front.next = node, node
        self._size += 1

    def insertRear(self, key):
        node = ListNode(key, self.rear.prev, self.rear)
        self.rear.prev.next, self.rear.prev = node, node
        self._size += 1

    def deleteFront(self):
        if self._size == 0:
            return
        self.front.next.next.prev, self.front.next = self.front, self.front.next.next
        self._size -= 1

    def deleteRear(self):
        if self._size == 0:
            return
        self.rear.prev.prev.next, self.rear.prev = self.rear, self.rear.prev.prev
        self._size -= 1

    def getFront(self):
        return self.front.next if self._size > 0 else None

    def getRear(self):
        return self.rear.prev if self._size > 0 else None

    def isEmpty(self):
        return self._size == 0

    def size(self):
        return self._size
    
    def __str__(self):
        res = []
        if self._size == 0:
            return ",".join(res)
        temp = self.front.next
        while temp != self.rear:
            res.append(str(temp.val))
            temp = temp.next
        return ",".join(res)

dq = MyDeque()
dq.insertFront(100)
dq.insertFront(200)

print(dq)

dq.deleteFront()
print(dq)

dq.insertRear(200)
print(dq)

print(dq.getFront().val)
print(dq.getRear().val)
