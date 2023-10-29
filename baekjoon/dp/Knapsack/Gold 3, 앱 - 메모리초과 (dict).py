# https://www.acmicpc.net/problem/7579

from sys import maxsize
from itertools import product

N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

dp = {(0, 0):cost[0]}
for row in range(1, M+1):
    dp[(row, 0)] = maxsize if memory[0]<row else cost[0]
for col in range(1, N):
    dp[(0, col)] = min(dp[(0, col-1)], cost[col-1])

for row, col in product(range(1, M+1), range(1, N)):
        dp[(row, col)] = min(
            dp[(row, col-1)],
            dp[(row-memory[col], col-1)] + cost[col]
        ) if row-memory[col]>=0 else dp[(row, col-1)]

print(dp[(M, N-1)])