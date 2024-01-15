from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solution(maps):
    N, M = len(maps), len(maps[0])

    q = deque([(0, 0, 1)])
    visited = [[False]*M for _ in range(N)]
    visited[0][0] = True
    
    while q:
        y, x, cnt = q.popleft()
        if (y, x) == (N-1, M-1):
            return cnt
        
        for u, v in zip(dy, dx):
            ny, nx = y+u, x+v
            if 0<=ny<N and 0<=nx<M and maps[ny][nx] and not visited[ny][nx]:
                q.append((ny, nx, cnt+1))
                visited[ny][nx] = True            
                
    return -1