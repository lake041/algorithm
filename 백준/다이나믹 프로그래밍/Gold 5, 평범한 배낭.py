# https://www.acmicpc.net/problem/12865
# 최적의 원리가 성립하는가

from itertools import product
from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
weight = []
value = []
for _ in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

dp = [[0]*(K+1) for _ in range(N)]
for num, limit in product(range(N), range(1, K+1)):
    if num == 0:
        if weight[num]<=limit:
            dp[num][limit] = value[num]
        continue
    if limit-weight[num] >= 0:        
        dp[num][limit] = max(dp[num-1][limit], value[num] + dp[num-1][limit-weight[num]])
    else:
        dp[num][limit] = dp[num-1][limit]
print(dp[N-1][K])

'''
4 7
6 13
4 8
3 6
5 12

14
'''