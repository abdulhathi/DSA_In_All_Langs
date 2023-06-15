class MinStack:
    def __init__(self):
        self.mainSt = []
        self.auxSt = []
        
    def push(self, val: int) -> None:
        if not self.mainSt or (self.auxSt and val <= self.auxSt[-1]):
            self.auxSt.append(val)
        self.mainSt.append(val)
                              
    def pop(self) -> None:
        if self.mainSt:
            val = self.mainSt.pop()
            if self.auxSt and self.auxSt[-1] == val:
                self.auxSt.pop()

    def top(self) -> int:
        if self.mainSt:
            return self.mainSt[-1]

    def getMin(self) -> int:
        if self.auxSt:
            return self.auxSt[-1]
        
minStack = None
res = []
keys = ["MinStack","push","push","push","getMin","pop","top","getMin"]
values = [[],[-2],[0],[-3],[],[],[],[]]
for key, value in zip(keys, values):
    match key:
        case "MinStack":
            minStack = MinStack()
            res.append(None)
        case "push":
            minStack.push(value[0])
            res.append(None)
        case "top":
            res.append(minStack.top())
        case "pop":
            res.append(minStack.pop())
        case "getMin":
            res.append(minStack.getMin())
print(res)
