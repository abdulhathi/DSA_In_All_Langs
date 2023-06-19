import math

class BinaryHeap:
    def __init__(self, arr=[]):
        self.li = arr
        i = (len(arr)-2)//2
        for i in range(i, -1, -1):
            self.minHeapify(i)

    def parent(self, i):
        return (i-1)//2
    
    def lChild(self, i):
        return (2*i) + 1
    
    def rChild(self, i):
        return (2*i) + 2
    
    def bubbleUp(self, i):
        li, x = self.li, self.li[i]
        p = self.parent(i)
        while p >= 0 and li[p] > x:
            li[i], li[p] = li[p], li[i]
            i = p
            p = self.parent(i)

    # Time : O(logn)
    def insert(self, x):
        self.li.append(x)
        self.bubbleUp(len(self.li)-1)
        
    def minHeapify(self, i):
        li, n = self.li, len(self.li)
        l, r = self.lChild(i), self.rChild(i)
        while l < n and li[l] < li[i]:
            if r < n and li[r] < li[l]:
                l = r
            li[l], li[i] = li[i], li[l]
            i = l
            l, r = self.lChild(i), self.rChild(i)
        
    def delete(self, i):
        if not self.li:
            return
        self.decreaseKey(i, -math.inf)
        self.extractMin()
        
    def extractMin(self):
        if not self.li:
            return math.inf
        li, lp, rp = self.li, 0, len(self.li)-1
        li[lp], li[rp] = li[rp], li[lp]
        res = li.pop()
        self.minHeapify(0)
        return res
    
    def decreaseKey(self,i,x):
        self.li[i] = x
        self.bubbleUp(i)

    def __str__(self):
        return ",".join([str(val) for val in self.li])
    
binaryHeap = BinaryHeap([10,20,15,40,50,100,25,45])
print(binaryHeap)
binaryHeap.insert(12)
print(binaryHeap)
print(binaryHeap.extractMin())
print(binaryHeap)

binaryHeap = BinaryHeap([20,25,30,35,40,80,32,100,70,60])
print(binaryHeap)
print(binaryHeap.extractMin())
print(binaryHeap)

binaryHeap = BinaryHeap([10,20,40,80,100,70])
binaryHeap.decreaseKey(3, 5)
print(binaryHeap)

binaryHeap = BinaryHeap([20,80,200,90,100,250,500,120])
binaryHeap.decreaseKey(3, 10)
print(binaryHeap)

binaryHeap = BinaryHeap([10,20,30,40,50,35,38,45])
binaryHeap.delete(3)
print(binaryHeap)