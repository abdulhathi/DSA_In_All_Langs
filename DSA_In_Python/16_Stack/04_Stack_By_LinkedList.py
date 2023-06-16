from ListNode import ListNode

class StackByLL:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, val):
        node = ListNode(val, None, self.head)
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

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0
        
stackByLL = None
keys = ["StackByLL","push","push","push","pop","peek","size"]
values = [[],[10],[20],[30],[],[],[]]
res = []
for key,value in zip(keys,values):
    match key:
        case "StackByLL":
            stackByLL = StackByLL()
            res.append(None)
        case "push":
            stackByLL.push(value[0])
            res.append(None)
        case "pop":
            res.append(stackByLL.pop())
        case "peek":
            res.append(stackByLL.peek())
        case "size":
            res.append(stackByLL.getSize())
print(res)