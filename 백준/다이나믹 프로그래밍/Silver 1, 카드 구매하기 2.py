# https://www.acmicpc.net/problem/16194

from sys import stdin
input = stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))
dp = [0]*(N+1)

dp[1] = P[1]
for i in range(1, N+1):
    temp = P[i]
    for j in range(1, i):
        temp = min(temp, P[i-j] + dp[j])
    dp[i] = temp
print(dp[N])