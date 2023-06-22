
n = 5
parent = [i for i in range(n)]
rank = [0] * n

def find(i):
    if parent[i] == i:
        return parent[i]
    parent[i] = find(parent[i])
    return parent[i]

def union(u, v):
    pU, pV = find(u), find(v)
    if rank[pU] > rank[pV]:
        parent[pV] = pU
    elif rank[pV] > rank[pU]:
        parent[pU] = pV
    else:
        parent[pV] = pU
        rank[pU] += 1


# make frient 1,4
union(1,4)
print(parent, rank)

union(4,3)
print(parent, rank)

union(0,2)
print(parent, rank)

union(0,1)
print(parent, rank)

find(3)
print(parent, rank)

find(2)
print(parent, rank)

find(4)
print(parent, rank)