# https://www.acmicpc.net/problem/2294

from math import inf
from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
coins = list(set([int(input()) for _ in range(N)]))
coins.sort()
leng = len(coins)
dp = [0] + [inf]*K

for i in range(1, K+1):
    for coin in coins:
        if coin > K:
            break
        else:
            dp[i] = min(dp[i], dp[i-coin] + 1)
print(-1 if dp[K]==inf else dp[K])

'''
    0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15
1   0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15
5   0   0   0   0   0   1   2   3   4   5   2   3   4   5   6   3
12  0   0   0   0   0   0   0   0   0   0   0   0   1   2   3   4
'''