from collections import deque

dq = deque()
# append left
dq.appendleft(10)
dq.appendleft(20)
print(dq)

# append right
dq.append(100)
dq.append(200)
print(dq)

# Pop right
print(dq.pop())
print(dq)

# Pop left
print(dq.popleft())

# Insert
dq.insert(1,1000)
print(dq)

dq.extendleft([1212,123232])
print(dq)

dq.extend([4444,5555])
print(dq)

print(dq[3])
