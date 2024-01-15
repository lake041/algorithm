from collections import deque, defaultdict

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(N)]

time = 0

while True:
    q = deque([(0, 0)])
    visited = [[False]*M for _ in range(N)]
    chiz = defaultdict(int)

    while q:
        y, x = q.popleft()
        for u, v in zip(dy, dx):
            ny, nx = y+u, x+v
            if 0<=ny<N and 0<=nx<M and not visited[ny][nx]:
                if bod[ny][nx]:
                    chiz[(ny, nx)] += 1
                else:
                    q.append((ny, nx))
                    visited[ny][nx] = True
    
    if not chiz:
        break

    time += 1
    for (y, x), count in chiz.items():
        if count >= 2:
            bod[y][x] = 0

print(time)