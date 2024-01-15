# https://www.acmicpc.net/problem/7569

from itertools import product
from collections import deque

M, N = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

ans = 0
tomatos = deque((y, x, 0) for y, x in product(range(N), range(M)) if bod[y][x]==1)

while tomatos:
    y, x, day = tomatos.popleft()
    ans = max(ans, day)

    for u, v in zip(dy, dx):
        ny, nx = y+u, x+v
        if 0<=ny<N and 0<=nx<M and not bod[ny][nx]:
            tomatos.append((ny, nx, day+1))
            bod[ny][nx] = 1

print(-1 if any(not bod[y][x] for y, x in product(range(N), range(M))) else day)