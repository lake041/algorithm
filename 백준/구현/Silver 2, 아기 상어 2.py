# https://www.acmicpc.net/problem/17086

from collections import deque
from itertools import product
from sys import stdin
input = stdin.readline

dy = [-1, 0, 1, 0, -1, -1, 1, 1]
dx = [0, -1, 0, 1, -1, 1, -1, 1]

N, M = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(N)]

q = deque()
for y, x in product(range(N), range(M)):
    if bod[y][x] == 1:
        q.append((y, x))

count = 0
while q:
    for _ in range(len(q)):
        y, x = q.popleft()
        for u, v in zip(dy, dx):
            ny, nx = y+u, x+v
            if not(0<=ny<N and 0<=nx<M and bod[ny][nx]==0):
                continue
            q.append((ny, nx))
            bod[ny][nx] = 1
    if q == deque([]):
        break
    count += 1
print(count)