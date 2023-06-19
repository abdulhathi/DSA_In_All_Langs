import heapq

pq = [5,20,1,30,4]
heapq.heapify(pq)
print(pq)

heapq.heappush(pq, 35)
print(pq)

print(heapq.heappop(pq))
print(pq)

# Nlargest and Nsmallest
print(heapq.nlargest(2,pq))
print(heapq.nsmallest(3,pq))

print(pq)
print(heapq.heappushpop(pq, 6))
print(pq)

print(heapq.heapreplace(pq, -1))
print(pq)