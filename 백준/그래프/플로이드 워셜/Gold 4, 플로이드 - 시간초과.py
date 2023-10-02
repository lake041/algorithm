# https://www.acmicpc.net/problem/11404
# PyPy 3: 288ms
# Python 3 시간초과

from math import inf
from itertools import product

N = int(input())
M = int(input())
cost = [[inf]*N for _ in range(N)]
for _ in range(M):
    i, j, k = map(int, input().split())
    cost[i-1][j-1] = min(cost[i-1][j-1], k)

for k in range(N):
    for i, j in product(range(N), range(N)):
        if i == j:
            continue
        if cost[i][j] > cost[i][k] + cost[k][j]:
            cost[i][j] = cost[i][k] + cost[k][j]

for i, j in product(range(N), range(N)):
    if cost[i][j] == inf:
        cost[i][j] = 0

for row in cost:
    print(' '.join(map(str, row)))