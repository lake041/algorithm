from collections import deque
from itertools import product

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solution(board):
    bod = [list(row) for row in board]
    R, C = len(bod), len(bod[0])
    
    sy, sx = next((y, x) for y, x in product(range(R), range(C)) if bod[y][x] == 'R')
    ty, tx = next((y, x) for y, x in product(range(R), range(C)) if bod[y][x] == 'G')
    
    q = deque([(sy, sx, 0)])
    visited = [[False]*C for _ in range(R)]
    visited[sy][sx] = True
    
    def can_slide(y, x):
        return 0<=y<R and 0<=x<C and bod[y][x]!="D"
    
    while q:
        y, x, cnt = q.popleft()
        if bod[y][x] == "G":
            return cnt
        for u, v in zip(dy, dx):
            ny, nx = y, x
            while can_slide(ny + u, nx + v):
                ny, nx = ny + u, nx + v
            if not visited[ny][nx]:
                q.append((ny, nx, cnt+1))
                visited[ny][nx] = True
        
    return -1