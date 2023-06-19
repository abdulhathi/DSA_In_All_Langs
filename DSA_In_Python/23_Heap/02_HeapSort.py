def heapSort(li):
    def maxHeapify(li, n, i):
        l, r = (i*2) + 1, (i*2) + 2
        while l < n and li[l] > li[i]:
            l = r if r < n and li[r] > li[l] else l
            li[l], li[i] = li[i], li[l]
            i = l
            l, r = (i*2) + 1, (i*2) + 2            
    
    def buildHeap(li):
        for i in range((len(li)-2)//2, -1, -1):
            maxHeapify(li, len(li), i)

    buildHeap(li)
    for i in range(len(li)-1, -1, -1):
        li[i], li[0] = li[0], li[i]
        maxHeapify(li, i, 0)
    
    return li

print(heapSort([50,20,10,4,15]))