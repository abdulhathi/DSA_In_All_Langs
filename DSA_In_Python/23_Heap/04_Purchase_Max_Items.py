import heapq

def purchaseMaxItem(arr, sum):
    count = 0
    first = heapq.heappop(arr)
    heapq.heappush(arr, first)
    while sum > 0:
        val = heapq.heappop(arr)
        print(val)
        sum -= val
        count += 1
    return count if sum == 0 else count - 1

print(purchaseMaxItem([1,12,5,111,200],10))
print()
print(purchaseMaxItem([20,10,5,30,100],35))