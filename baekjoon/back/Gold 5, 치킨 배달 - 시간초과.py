from sys import maxsize
from collections import deque
from itertools import combinations, product

N, M = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(N)]

# 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.

houses = set()
chicks = set()
for row, col in product(range(N), range(N)):
    num = bod[row][col]
    if num == 1:
        houses.add((row, col))
    if num == 2:
        chicks.add((row, col))

def cal_dist(row, col, chicks, N):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    q = deque()
    q.append((row, col, 0))
    visited = [[False]*N for _ in range(N)]
    visited[row][col] = True
    while q:
        y, x, cnt = q.popleft()
        for u, v in zip(dy, dx):
            ny, nx = y+u, x+v
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
                if (ny, nx) in chicks:
                    return cnt+1
                else:
                    q.append((ny, nx, cnt+1))
                    visited[ny][nx] = True
    return False

ans = maxsize
for new_chicks in combinations(list(chicks), M):
    dist_sum = 0
    for row, col in houses:
        dist_sum += cal_dist(row, col, new_chicks, N)
    ans = min(ans, dist_sum)
print(ans)