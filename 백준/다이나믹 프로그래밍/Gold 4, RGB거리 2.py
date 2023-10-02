from math import inf
from sys import stdin
input = stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

dp0 = [[cost[0][0], inf, inf] for _ in range(N)]
dp1 = [[inf, cost[0][1], inf] for _ in range(N)]
dp2 = [[inf, inf, cost[0][2]] for _ in range(N)]

def foo(target, index):
    for color in range(3):
        target[index][color] = min(target[index-1][(color+1)%3], target[index-1][(color+2)%3]) + cost[index][color]

for i in range(1, N):
    foo(dp0, i)
    foo(dp1, i)
    foo(dp2, i)

x = min(dp0[N-1][1], dp0[N-1][2], dp1[N-1][0], dp1[N-1][2], dp2[N-1][0], dp2[N-1][1])
print(x)