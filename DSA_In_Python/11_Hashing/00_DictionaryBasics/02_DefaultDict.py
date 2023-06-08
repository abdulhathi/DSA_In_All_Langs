from collections import defaultdict

dic = defaultdict(int)

for c in "abdul":
    dic[c] += 1

print(dic)