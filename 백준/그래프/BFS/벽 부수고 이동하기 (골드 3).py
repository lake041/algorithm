from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
bod = [list(map(int, list(input()))) for _ in range(N)]

q = deque([(0, 0, 1, False)])
v1 = [[False]*M for _ in range(N)]
v2 = [[False]*M for _ in range(N)]

ans = -1

while q:
    y, x, cnt, done = q.popleft()
    if (y, x) == (N-1, M-1):
        ans = cnt
        break

    for u, v in zip(dy, dx):
        ny, nx = y+u, x+v
        if not(0<=ny<N and 0<=nx<M):
            continue
        if not bod[ny][nx] and not done and not v1[ny][nx]:
            q.append((ny, nx, cnt+1, done))
            v1[ny][nx] = True
        if not bod[ny][nx] and done and not v2[ny][nx]:
            q.append((ny, nx, cnt+1, done))
            v2[ny][nx] = True
        if bod[ny][nx] and not done and not v2[ny][nx]:
            q.append((ny, nx, cnt+1, True))
            v2[ny][nx] = True

print(ans)