from collections import deque
from itertools import product
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(N)]
# 2: 목표, 1: 갈 수 있는 땅, 0: 갈 수 없는 땅

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for y, x in product(range(N), range(M)):
    if bod[y][x] == 2:
        (ty, tx) = (y, x)

visited = [[False]*M for _ in range(N)]
answer = [[0]*M for _ in range(N)]
q = deque()
q.append((ty, tx))
visited[ty][tx] = True
answer[ty][tx] = 0

while q:
    y, x = q.popleft()
    for u, v in zip(dy, dx):
        ny, nx = y+u, x+v
        if not(0<=ny<N and 0<=nx<M and visited[ny][nx]==False):
            continue
        visited[ny][nx] = True
        if bod[ny][nx] == 0:
            answer[ny][nx] = 0
            continue
        answer[ny][nx] = answer[y][x] + 1
        q.append((ny, nx))

for y, x in product(range(N), range(M)):
    if bod[y][x]==1 and visited[y][x]==False:
        answer[y][x] = -1

for row in answer:
    print(*row)

'''
15 15
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
'''
