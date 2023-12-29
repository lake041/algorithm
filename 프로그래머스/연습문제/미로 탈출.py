from collections import deque
from itertools import product

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solution(maps):
    bod = [list(row) for row in maps]
    R, C = len(bod), len(bod[0])
    
    sy, sx = next((y, x) for y, x in product(range(R), range(C)) if bod[y][x] == "S")

    q = deque([(sy, sx, 0, False)])
    visited = [[False]*C for _ in range(R)]
    visited[sy][sx] = True
    
    while q:
        y, x, time, ok = q.popleft()
        
        if ok and bod[y][x] == "E":
            return time
        
        if not ok and bod[y][x] == "L":
            q = deque([(y, x, time, True)])
            visited = [[False]*C for _ in range(R)]
            visited[y][x] = True
            continue
        
        for u, v in zip(dy, dx):
            ny, nx = y+u, x+v
            if 0<=ny<R and 0<=nx<C and not visited[ny][nx] and bod[ny][nx]!="X":
                q.append((ny, nx, time+1, ok))
                visited[ny][nx] = True
        
    return -1