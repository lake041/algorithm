# https://www.acmicpc.net/problem/11727

from sys import stdin
input = stdin.readline

N = int(input())
dp = [0]*1001
dp[1] = 1
dp[2] = 3
for i in range(3, 1001):
    dp[i] = dp[i-1] + dp[i-2]*2
print(dp[N]%10007)