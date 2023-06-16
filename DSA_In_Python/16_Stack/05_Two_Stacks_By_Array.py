class TwoStackByArray:
    def __init__(self, size):
        self._size = size
        self.st = [None] * size
        self.st1 = -1
        self.st2 = size
    
    def push1(self, val):
        lp = self.st1 + 1
        if lp < self.st2:
            self.st[lp] = val
            self.st1 += 1

    def push2(self, val):
        rp = self.st2 - 1
        if rp > self.st1:
            self.st[rp] = val
            self.st2 -= 1
    
    def pop1(self):
        if self.st1 == -1:
            return None
        val = self.st[self.st1]
        self.st[self.st1] = None
        self.st1 -= 1
        return val
    
    def pop2(self):
        if self.st2 == self._size:
            return None
        val = self.st[self.st2]
        self.st[self.st2] = None
        self.st2 += 1
        return val
    
    def size1(self):
        return self.st1 + 1
    def size2(self):
        return self._size - (self.st2)
    
twoStack = None
keys = ["TwoStack", "push1", "push2", "push1", "push1", "pop1", "pop2", "size1", "size2"]
values = [[5],[1],[10],[2],[3],[],[],[],[]]
res = []
for key, value in zip(keys, values):
    match key:
        case "TwoStack":
            twoStack = TwoStackByArray(value[0])
            res.append(None)
        case "push1":
            twoStack.push1(value[0])
            res.append(None)
        case "push2":
            twoStack.push2(value[0])
            res.append(None)
        case "pop1":
            res.append(twoStack.pop1())
        case "pop2":
            res.append(twoStack.pop2())
        case "size1":
            res.append(twoStack.size1())
        case "size2":
            res.append(twoStack.size2())
print(res)