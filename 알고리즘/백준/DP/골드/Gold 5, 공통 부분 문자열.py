# https://www.acmicpc.net/problem/5582
# 최적의 원리가 성립하는가

from sys import stdin
input = stdin.readline

S1 = input().rstrip()
S2 = input().rstrip()
LS1 = len(S1)
LS2 = len(S2)

dp = [0]*(LS1+1)
ans = 0
for i in range(LS2):
    temp = [0]*(LS1+1)
    for j in range(LS1):
        if S1[j] == S2[i]:
            temp[j+1] = dp[j] + 1
    ans = max(ans, max(temp))
    dp = temp[:]
    print(dp)
print(ans)

'''
 ECADADABRBCRDARA
A
B
R
A
C01
A0020
D0003
A00004
B000004
R0000005
A
'''