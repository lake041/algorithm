# https://www.acmicpc.net/problem/7579

from sys import maxsize
from itertools import product

N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

'''
5 60
30 10 20 35 40
3 0 3 5 4
=> 6

총합이 M 이상인 임의의 메모리를 선택하여 cost 이하로 만들기
'''

# [row][col] => row 바이트 이상을 col 인덱스까지의 메모리로 만들 수 있는 최소 비용
dp = [[maxsize]*N for _ in range(M+1)]

# dp[row][col] => memory[col], cost[col]이 새로 추가된 상황
# case 1: memory[col]이 새로 추가된 게 더 싸다면,
# col-1까지 그리고 row-memory 바이트 이상일 때의 최솟값,
# 즉, dp[row-memory[col]][col-1] + cost[col]
# col >= 1이고 row-memory[col] >= 0일 때만

# case 2: memory[col]을 안 쓰는 게 더 싸다면,
# dp[row][col-1]
# 두 값 중 작은 값을 기록한다
# col >= 1일 때만

dp[0][0] = cost[0]
for row in range(1, M+1):
    dp[row][0] = maxsize if memory[0]<row else cost[0]
for col in range(1, N):
    dp[0][col] = min(dp[0][col-1], cost[col-1])

for row, col in product(range(1, M+1), range(1, N)):
    dp[row][col] = min(
        dp[row][col-1],
        dp[row-memory[col]][col-1] + cost[col]
    ) if row-memory[col]>=0 else dp[row][col-1]

print(dp[M][N-1])