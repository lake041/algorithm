# https://www.acmicpc.net/problem/2206

from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
bod = [list(map(int, input().rstrip())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

ans = -1
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
q = deque()
q.append((0, 0, 0)) # y, x, total, wall
visited[0][0][0] = 1
while q:
    y, x, wall = q.popleft()
    if (y, x) == (N-1, M-1):
        ans = visited[y][x][wall]
        break
    for u, v in zip(dy, dx):
        ny, nx = y+u, x+v
        if not (0<=ny<N and 0<=nx<M):
            continue
        if bod[ny][nx]==0 and visited[ny][nx][wall]==0:
            visited[ny][nx][wall] = visited[y][x][wall] + 1
            q.append((ny, nx, wall))
        if bod[ny][nx]==1 and wall==0:
            visited[ny][nx][1] = visited[y][x][0] + 1
            q.append((ny, nx, 1))
print(ans)