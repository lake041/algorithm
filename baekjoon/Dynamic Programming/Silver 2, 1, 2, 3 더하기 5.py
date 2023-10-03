# https://www.acmicpc.net/problem/15990
# 다시 볼만한 문제

from sys import stdin
input = stdin.readline

dp = [[0]*4 for _ in range(100001)]
dp[1][1], dp[1][2], dp[1][3] = 1, 0, 0
dp[2][1], dp[2][2], dp[2][3] = 0, 1, 0
dp[3][1], dp[3][2], dp[3][3] = 1, 1, 1
dp[4][1], dp[4][2], dp[4][3] = 2, 0, 1
for i in range(5, 100001):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3])%1000000009
    dp[i][2] = (dp[i-2][1] + dp[i-2][3])%1000000009
    dp[i][3] = (dp[i-3][1] + dp[i-3][2])%1000000009

T = int(input())
for _ in range(T):
    N = int(input())
    print((dp[N][1] + dp[N][2] + dp[N][3])%1000000009)