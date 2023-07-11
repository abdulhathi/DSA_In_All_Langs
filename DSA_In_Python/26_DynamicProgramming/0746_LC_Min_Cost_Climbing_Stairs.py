from collections import defaultdict

def minCostClimbingStairs(cost: list[int]) -> int:
    dp = defaultdict(int)
    dp[len(cost)], dp[len(cost)+1] = 0, 0

    def topDown(step):
        if step+1 >= len(cost) or step+2 >= len(cost):
            return 0
        if step in dp:
            return dp[step]
        oneStep = cost[step+1] + topDown(step+1)
        twoStep = cost[step+2] + topDown(step+2)
        dp[step] = min(oneStep, twoStep)
            
        return dp[step]
    
    return topDown(-1)

print(minCostClimbingStairs([10,15,20]))
