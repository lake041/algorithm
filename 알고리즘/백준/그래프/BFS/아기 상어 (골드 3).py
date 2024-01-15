from sys import stdin
from collections import deque
from itertools import product
input = stdin.readline

N = int(input())
bod = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

time = 0
size, stomach = 2, 0
sy, sx = next((y, x) for y, x in product(range(N), range(N)) if bod[y][x] == 9)
bod[sy][sx] = 0

def find_fish(sy, sx, size):
    q = deque([(sy, sx, 0)])
    visited = [[False]*N for _ in range(N)]
    visited[sy][sx] = True

    while q:
        fish = []
        for _ in range(len(q)):
            y, x, cnt = q.popleft()

            if 0 < bod[y][x] < size:
                fish.append((y, x, cnt))
                continue
        
            for u, v in zip(dy, dx):
                ny, nx = y+u, x+v
                if 0<=ny<N and 0<=nx<N and not visited[ny][nx] and bod[ny][nx]<=size:
                    q.append((ny, nx, cnt+1))
                    visited[ny][nx] = True

        if fish:
            fish.sort()
            return fish[0]

while True:
    fish = find_fish(sy, sx, size)
    if not fish:
        break

    fy, fx, dist = fish

    bod[fy][fx] = 0
    stomach += 1
    if size == stomach:
        size, stomach = size+1, 0
    time += dist
    sy, sx = fy, fx

print(time)
