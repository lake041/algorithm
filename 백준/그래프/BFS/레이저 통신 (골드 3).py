# 같은 도착지를 같은 cost에 도착해도 이전 경로에 따라 더 빠른 경로가 있을 수 있다.

from sys import maxsize
from heapq import heappop, heappush
from itertools import product

C, R = map(int, input().split())
bod = [list(input()) for _ in range(R)]
mirror = [[[maxsize]*4 for _ in range(C)] for _ in range(R)]

dots = [(y, x) for y, x in product(range(R), range(C)) if bod[y][x] == "C"]
sy, sx = dots[0]
ty, tx = dots[1]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

q = [(sy, sx, -1, -1)]
for i in range(4):
    mirror[sy][sx][i] = 0

while q:
    y, x, cnt, dir = heappop(q)

    if (y, x) == (ty, tx):
        mirror[ty][tx][dir] = min(mirror[ty][tx][dir], cnt)

    for i in range(4):
        u, v = dy[i], dx[i]
        ny, nx = y, x
        while 0<=ny+u<R and 0<=nx+v<C and bod[ny+u][nx+v] != "*" and cnt + 1 < mirror[ny+u][nx+v][i] :
            ny, nx = ny+u, nx+v
            heappush(q, (ny, nx, cnt + 1, i))
            mirror[ny][nx][i] = cnt + 1

print(min(mirror[ty][tx]))