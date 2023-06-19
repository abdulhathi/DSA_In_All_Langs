import heapq

def medianOfStream(nums):
    miH, mxH, median = [], [], []
    for num in nums:
        heapq.heappush(mxH, -num)
        heapq.heappush(miH, -heapq.heappop(mxH))
        if len(mxH) < len(miH):
            heapq.heappush(mxH, -heapq.heappop(miH))
        
        median.append(((-mxH[0])+miH[0])/2 if len(mxH) == len(miH) else -mxH[0])
    
    return median

print(medianOfStream([25,7,10,15,20]))
