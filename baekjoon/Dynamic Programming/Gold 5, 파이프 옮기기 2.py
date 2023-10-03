# https://www.acmicpc.net/problem/17070
# 엣지 케이스

from itertools import product
from sys import stdin
input = stdin.readline

'''
16
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

16
0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
''' 

N = int(input())
bod = [list(map(int, input().split())) for _ in range(N)]

for y, x in product(range(N), repeat=2):
    if bod[y][x] == 0:
        bod[y][x] = [0, 0, 0]
bod[0][1] = [1, 0, 0]

def valid(y, x):
    return True if 0<=y<N and 0<=x<N and bod[y][x]!=1 else False

def check(y, x):
    temp = [0, 0, 0]
    if bod[y][x]==1: return
    if valid(y, x-1):
        temp[0] += bod[y][x-1][0] + bod[y][x-1][1]
    if valid(y-1, x-1) and valid(y-1, x) and valid(y, x-1):
        temp[1] += sum(bod[y-1][x-1])
    if valid(y-1, x):
        temp[2] += bod[y-1][x][1] + bod[y-1][x][2]
    bod[y][x] = temp

for row in range(N):
    for col in range(1, N):
        if (row, col) == (0, 1):
            continue
        check(row, col)
# for row in bod:
#     print(row)
if bod[N-1][N-1] != 1:
    print(sum(bod[N-1][N-1]))
else:
    print(0)

'''
ㅁㅁㅁㅁ
ㅁㅁㅁㅁ
ㅁㅁㅇㅁ
'''