# https://www.acmicpc.net/problem/9251

from sys import stdin
input = stdin.readline

S1 = list(' ' + input().rstrip())
S2 = list(' ' + input().rstrip())

SL1 = len(S1)
SL2 = len(S2)

dp = [[0]*SL1 for _ in range(SL2)]
for row in range(1, SL2):
    for col in range(1, SL1):
        if S1[col] == S2[row]:
            dp[row][col] = dp[row-1][col-1] + 1
        else:
            dp[row][col] = max(dp[row-1][col], dp[row][col-1])
print(dp[row][col])

'''
ACAYKP
CAPCAK

ACAYKP
C010000
A101000
P000001
C
A
K
'''