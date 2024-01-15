# https://www.acmicpc.net/problem/11726
# 문제 좀 읽자

from sys import stdin
input = stdin.readline

N = int(input())
dp = [0]*1001
dp[1] = 1
dp[2] = 2
for i in range(3, 1001):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[N]%10007)