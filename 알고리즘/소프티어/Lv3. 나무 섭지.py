from sys import stdin, maxsize
from collections import deque
from itertools import product
input = stdin.readline

N, M = map(int, input().split())
bod = [list(input().rstrip()) for _ in range(N)]

ghost = [(y, x) for y, x in product(range(N), range(M)) if bod[y][x] == "G"]
ty, tx = next((y, x) for y, x in product(range(N), range(M)) if bod[y][x] == "D")
sy, sx = next((y, x) for y, x in product(range(N), range(M)) if bod[y][x] == "N")

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

shortest_of_ghost = maxsize
shortest_of_namoo = maxsize

q = deque([(sy, sx, 0)])
visited = [[False]*M for _ in range(N)]
visited[sy][sx] = True

while q:
    y, x, cnt = q.popleft()
    
    if (y, x) == (ty, tx):
        shortest_of_namoo = cnt
        break

    for u, v in zip(dy, dx):
        ny, nx = y+u, x+v
        if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and bod[ny][nx] != '#':
            q.append((ny, nx, cnt+1))
            visited[ny][nx] = True

for gy, gx in ghost:
    shortest_of_ghost = min(shortest_of_ghost, abs(ty-gy) + abs(tx-gx))

print("Yes" if shortest_of_namoo < shortest_of_ghost else "No")