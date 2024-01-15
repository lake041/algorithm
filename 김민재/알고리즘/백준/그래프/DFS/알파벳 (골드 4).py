# 전체를 함수로 감싸면 실행시간 더 줄어듦

from sys import stdin
from collections import deque
input = stdin.readline

R, C = map(int, input().split())
bod = [list(map(lambda x: 1 << (ord(x)-65), list(input().rstrip()))) for _ in range(R)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

memo = [[set() for _ in range(C)] for _ in range(R)]

q = deque([(0, 0, bod[0][0], 1)])
ans = 0

while q:
    y, x, visited, cnt = q.popleft()
    ans = max(ans, cnt)
    if ans == 26:
        break

    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=ny<R and 0<=nx<C and not visited & bod[ny][nx]:
            next_visited = visited | bod[ny][nx]
            if next_visited not in memo[ny][nx]:
                q.append((ny, nx, next_visited, cnt+1))
                memo[ny][nx].add(next_visited)

print(ans)