from itertools import product
from collections import deque, defaultdict
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
bod = [list(map(int, list(input().rstrip()))) for _ in range(N)]
ans = [[0]*M for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

index = 1
count = defaultdict(int)
for y, x in product(range(N), range(M)):
    if bod[y][x] > 0:
        continue
    index += 1

    q = deque()
    q.append((y, x))
    bod[y][x] = index
    count[index] += 1
    while q:
        ty, tx = q.popleft()
        for u, v in zip(dy, dx):
            ny, nx = ty+u, tx+v
            if 0<=ny<N and 0<=nx<M and bod[ny][nx]==0:
                q.append((ny, nx))
                bod[ny][nx] = index
                count[index] += 1

for y, x in product(range(N), range(M)):
    if bod[y][x] != 1:
        continue
    count_set = set()

    q = deque()
    for u, v in zip(dy, dx):
        ny, nx = y+u, x+v
        if 0<=ny<N and 0<=nx<M and bod[ny][nx]!=1:
            count_set.add(bod[ny][nx])
    
    total_count = 0
    for index in count_set:
        total_count += count[index]
    ans[y][x] = (total_count+1)%10

for row in ans:
    print(''.join(map(str, row)))

# 시간초과
# for y, x in product(range(N), range(M)):
#     if bod[y][x] == 0:
#         continue
#     visited = [[False]*M for _ in range(N)]
#     bod[y][x] = 0

#     q = deque()
#     q.append((y, x))
#     visited[y][x] = True
#     count = 1
#     while q:
#         ty, tx = q.popleft()
#         for u, v in zip(dy, dx):
#             ny, nx = ty+u, tx+v
#             if 0<=ny<N and 0<=nx<M and bod[ny][nx]==0 and visited[ny][nx]==False:
#                 q.append((ny, nx))
#                 visited[ny][nx] = True
#                 count += 1
#     bod[y][x] = 1
#     ans[y][x] = count%10

# for row in ans:
#     print(''.join(map(str, row)))