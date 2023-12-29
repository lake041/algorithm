from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solution(maps):
    h = len(maps)
    w = len(maps[0])

    answer = -1
    visited = [[False]*w for _ in range(h)]
    q = deque([(0, 0, 1)])
    while q:
        y, x, cnt = q.popleft()
        if (y, x) == (h-1, w-1):
            answer = cnt
            break
        
        for u, v in zip(dy, dx):
            ny, nx = y+u, x+v
            if 0<=ny<h and 0<=nx<w and maps[ny][nx]==1 and visited[ny][nx]==False:
                visited[ny][nx] = True
                q.append((ny, nx, cnt+1))
    
    return answer