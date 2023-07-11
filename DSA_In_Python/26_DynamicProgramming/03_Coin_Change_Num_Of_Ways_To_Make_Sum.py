from collections import defaultdict

def coinChangeNumOfWays(coins, sumVal):
    memo = defaultdict(int)

    def topDown(i, s):
        if (i, s) in memo:
            return memo[(i, s)]
        if s < 0:
            memo[(i, s)] = 0
        elif s == 0:
            memo[(i, s)] = 1
        elif i == len(coins):
            memo[(i, s)] = 0
        else:
            memo[(i, s)] = topDown(i, s-coins[i]) + topDown(i+1, s)
        return memo[(i, s)]
    
    return topDown(0, sumVal)

print(coinChangeNumOfWays([1,2,3], 4))

def coinChangeNumOfWaysBottomUp(coins, sumVal):
    dp = defaultdict(int)
    m, n = len(coins)+1, sumVal + 1
    for r in range(m):
        dp[(r,0)] = 1
    
    for r in range(1, m):
        for c in range(1, n):
            coin = coins[r-1]
            if coin <= c:
                dp[(r,c)] = dp[(r-1,c)] + dp[(r,c-coin)]
            else:
                dp[(r,c)] = dp[(r-1,c)]
    return dp[(m-1,n-1)]

print(coinChangeNumOfWaysBottomUp([1,2,3], 4))


def change(amount: int, coins: list[int]) -> int:
    dp = defaultdict(int)

    def topDown(i, val, n):
        if val < 0:
            return 0
        elif val == 0:
            return 1
        res = 0
        for j in range(i, n):
            res += topDown(j, val-coins[j], n)
        return res
    
    return topDown(0, amount, len(coins))

print(change(5, [1,2,5]))