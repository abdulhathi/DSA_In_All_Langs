from collections import defaultdict

def fib(n):
    memo = defaultdict(int)
    memo[0], memo[1] = 0, 1

    def dfs(n):
        if n not in memo:
            memo[n] = dfs(n-1) + dfs(n-2)
        return memo[n]
    
    return dfs(n)

print(fib(5))
print(fib(7))

"""
    n = 0 1 2 3 4 5 6 7
        0 1 1 2 3 5 8 13
"""

def fib_Tab(n):
    tab = defaultdict(int)
    tab[0], tab[1] = 0, 1
    for i in range(2, n+1):
        tab[i] = tab[i-1] + tab[i-2]
    return tab[n]


print(fib_Tab(5))
print(fib_Tab(7))