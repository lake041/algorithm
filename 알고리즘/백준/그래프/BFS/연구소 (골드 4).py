from collections import deque
from itertools import product, combinations

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(N)]
safes = [(y, x) for y, x in product(range(N), range(M)) if bod[y][x] == 0]
virus = [(y, x) for y, x in product(range(N), range(M)) if bod[y][x] == 2]
sizes = []

for walls in combinations(safes, 3):
    for y, x in walls:
        bod[y][x] = 1
    
    q = deque(virus)
    while q:
        y, x = q.popleft()
        for u, v in zip(dy, dx):
            ny, nx = y+u, x+v
            if 0<=ny<N and 0<=nx<M and not bod[ny][nx]:
                q.append((ny, nx))
                bod[ny][nx] = 2

    size = sum([1 for y, x in product(range(N), range(M)) if not bod[y][x]])
    sizes.append(size)

    for y, x in safes:
        bod[y][x] = 0

print(max(sizes))