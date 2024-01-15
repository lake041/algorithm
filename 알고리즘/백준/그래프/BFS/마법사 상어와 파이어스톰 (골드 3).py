# https://www.acmicpc.net/problem/20058
# Python: 3856ms
# PyPy: 1296ms

from sys import stdin
from collections import deque
from itertools import product
input = stdin.readline

N, _ = map(int, input().split())
original_N, N = N, 2**N
bod = [list(map(int, input().split())) for _ in range(N)]
storm = list(map(int, input().split()))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

side = [[[] for _ in range(N)] for _ in range(N)]
for y, x in product(range(N), repeat=2):
    side[y][x] = [(ny, nx) for u, v in zip(dy, dx) if 0<=(ny:=y+u)<N and 0<=(nx:=x+v)<N]

rotated_dot = [[] for _ in range(original_N+1)]
for L in range(original_N+1):
    rotated_dot[L] = [[(0, 0) for _ in range(N)] for _ in range(N)]
    size = 2**L
    for y, x in product(range(0, N, size), repeat=2):
        for u, v in product(range(size), repeat=2):
            rotated_dot[L][y+u][x+v] = (y+v, x+size-1-u)

for L in storm:
    new_bod = [[0]*N for _ in range(N)]
    size = 2**L
    for y, x in product(range(N), repeat=2):
        ny, nx = rotated_dot[L][y][x]
        new_bod[ny][nx] = bod[y][x]
    bod = new_bod

    targets = []
    for y, x in product(range(N), repeat=2):
        if not bod[y][x]:
            continue
        ice = sum(1 for ny, nx in side[y][x] if bod[ny][nx])
        if ice < 3:
            targets.append((y, x))
    for y, x in targets:
        bod[y][x] -= 1
    
SUM, CHUNK = 0, 0
visited = [[False]*N for _ in range(N)]
for y, x in product(range(N), repeat=2):
    SUM += bod[y][x]
    if visited[y][x] or not bod[y][x]:
        continue
    q = deque([(y, x)])
    visited[y][x] = True
    cnt = 1
    while q:
        ty, tx = q.popleft()
        for ny, nx in side[ty][tx]:
            if bod[ny][nx] and not visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = True
                cnt += 1
    CHUNK = max(CHUNK, cnt)

print(SUM)
print(CHUNK)