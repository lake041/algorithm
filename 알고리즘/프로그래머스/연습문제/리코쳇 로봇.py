from collections import deque
from itertools import product

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

def solution(bod):
    bod = [list(row) for row in bod]
    R, C = len(bod), len(bod[0])
    visited = [[False]*C for _ in range(R)]
    
    sy, sx = next((y, x) for y, x in product(range(R), range(C)) if bod[y][x] == 'R')

    q = deque([(sy, sx, 0)])
    visited[sy][sx] = True
    
    while q:
        y, x, cnt = q.popleft()
        
        if bod[y][x] == 'G':
            return cnt
        
        for u, v in zip(dy, dx):
            ny, nx = y, x
            while 0<=ny+u<R and 0<=nx+v<C and bod[ny+u][nx+v] != 'D':
                ny, nx = ny+u, nx+v
            if not visited[ny][nx]:
                q.append((ny, nx, cnt+1))
                visited[ny][nx] = True
                
    return -1