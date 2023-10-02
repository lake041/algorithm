# https://www.acmicpc.net/problem/1799

from copy import deepcopy

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def check(bod, row, col):
    dy = [1, -1, 1, -1]
    dx = [1, -1, -1, 1]

    bod[row][col] = 2
    for i in range(1, N):
        for u, v in zip(dy, dx):
            ny, nx = row+u*i, col+v*i
            if 0<=ny<N and 0<=nx<N:
                bod[ny][nx] = 0
    return bod

def go(bod, row, col, cnt):
    global ans
    if row == N:
        ans = max(ans, cnt)
        return
    
    if col < N-1:
        if bod[row][col] == 1:
            go(check(deepcopy(bod), row, col), row, col+1, cnt+1)
        go(deepcopy(bod), row, col+1, cnt)

    else:
        if bod[row][col] == 1:
            go(check(deepcopy(bod), row, col), row+1, 0, cnt+1)
        go(deepcopy(bod), row+1, 0, cnt)

go(board, 0, 0, 0)
print(ans)

'''
5
1 1 0 1 1
0 1 0 0 0
1 0 1 0 1
1 0 0 0 0
1 0 1 1 1
7

3
0 1 1
1 1 1
1 1 1
4

4
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
6

5
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
8

10
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
18
'''