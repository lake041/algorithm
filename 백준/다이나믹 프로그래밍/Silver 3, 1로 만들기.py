# https://www.acmicpc.net/problem/1463
# N까지만 계산해도 충분하다

from math import inf
from sys import stdin
input = stdin.readline

dp = [0]*1000001
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2
for i in range(5, 1000001):
    answer = inf
    if i%3 == 0:
        answer = min(answer, dp[i//3]+1)
    if i%2 == 0:
        answer = min(answer, dp[i//2]+1)
    answer = min(answer, dp[i-1]+1)
    dp[i] = answer
print(dp[int(input())])