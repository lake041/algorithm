# https://www.acmicpc.net/problem/10942

from sys import stdin
input = stdin.readline

N = int(input())
num = list(map(int, input().split()))
M = int(input())
dp = [[0]*(N) for _ in range(N)]

for i in range(N):
    for start in range(N-i):
        end = start + i
        if start == end:
            dp[start][end] = 1
        elif num[start] == num[end]:
            if start + 1 == end:
                dp[start][end] = 1
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])

'''
7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7
'''