# https://www.acmicpc.net/problem/16236

from collections import deque
from itertools import product
from sys import stdin
input = stdin.readline

N = int(input())
bod = [list(map(int, input().split())) for _ in range(N)]

for y, x in product(range(N), repeat=2):
    if bod[y][x]==9:
        sy, sx = y, x
        break

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def get_targets(sy, sx, size):
    targets = []
    check = [[False]*N for _ in range(N)]
    q = deque()
    q.append((0, sy, sx))
    check[sy][sx] = True
    while q:
        for _ in range(len(q)):
            dist, y, x = q.popleft()
            for u, v in zip(dy, dx):
                ny, nx = y+u, x+v
                if not (0<=ny<N and 0<=nx<N and check[ny][nx]==False and bod[ny][nx]<=size):
                    continue
                if 0 < bod[ny][nx] < size:
                    targets.append((dist+1, ny, nx))
                else:
                    q.append((dist+1, ny, nx))
                check[ny][nx] = True
        if targets:
            break
    targets.sort()
    return targets

time = 0
size = 2
stomach = 0
while True:
    targets = get_targets(sy, sx, size)
    if targets == []:
        break

    dist, ty, tx = targets[0]
    bod[sy][sx] = 0
    bod[ty][tx] = 9
    sy, sx = ty, tx
    time += dist
    stomach += 1
    if stomach == size:
        size += 1
        stomach = 0
print(time)