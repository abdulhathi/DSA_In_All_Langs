from collections import defaultdict
import math

class Solution:
    def minTransfers(self, transactions: list[list[int]]) -> int:
        dic = defaultdict(int)
        minPID, maxPID = 0, 0
        for u,v,a in transactions:
          dic[u] -= a
          dic[v] += a
          minPID = min(minPID, u, v)
          maxPID = max(maxPID, u, v)


        def backtrack(i):
            nonlocal minPID, maxPID
            if i > maxPID:
                if sum([dic[key] for key in dic]) == 0:
                    return 0
                else:
                    return math.inf
            if dic[i] <= 0:
                return backtrack(i+1)
            
            minCount = math.inf
            for k in range(minPID, maxPID+1):
                count = 0
                for j in range(k, maxPID+1):
                    if i == j:
                        continue
                    if dic[j] < 0 and dic[j] <= dic[i]:
                        a = abs(dic[j])
                        dic[j] += a
                        dic[i] -= a
                        count += 1
                    if dic[i] == 0:
                        break
                minCount = min(count + backtrack(i+1), minCount)
            return minCount
            

        return backtrack(minPID)
    
print(Solution().minTransfers([[0,1,10],[2,0,5]]))