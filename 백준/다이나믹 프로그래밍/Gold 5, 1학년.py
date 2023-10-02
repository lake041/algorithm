# https://www.acmicpc.net/problem/5557
# 최적의 원리가 성립하는가

from sys import stdin
input = stdin.readline

N = int(input())
nums = list(map(int, input().split()))
dp = [[0]*(N-1) for _ in range(21)]

dp[nums[0]][0] = 1
for i in range(1, N-1):
    num = nums[i]
    for j in range(0, 21):
        if dp[j][i-1]==0:
            continue
        if 0<= j + num <= 20:
            dp[j+num][i] += dp[j][i-1]
        if 0<= j - num <= 20:
            dp[j-num][i] += dp[j][i-1]
print(dp[nums[-1]][N-2])