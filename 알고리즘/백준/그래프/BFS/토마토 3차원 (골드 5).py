# https://www.acmicpc.net/problem/7569

from itertools import product
from collections import deque

M, N, H = map(int, input().split())
bod = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dz = [0, 0, 0, 0, -1, 1]
dy = [-1, 0, 1, 0, 0, 0]
dx = [0, 1, 0, -1, 0, 0]

ans = 0
tomatos = deque((z, y, x, 0) for z, y, x in product(range(H), range(N), range(M)) if bod[z][y][x]==1)

while tomatos:
    z, y, x, day = tomatos.popleft()
    ans = max(ans, day)

    for w, u, v in zip(dz, dy, dx):
        nz, ny, nx = z+w, y+u, x+v
        if 0<=nz<H and 0<=ny<N and 0<=nx<M and not bod[nz][ny][nx]:
            tomatos.append((nz, ny, nx, day+1))
            bod[nz][ny][nx] = 1

print(-1 if any(not bod[z][y][x] for z, y, x in product(range(H), range(N), range(M))) else day)