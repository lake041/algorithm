from collections import deque
from itertools import product

def solution(maps):
    bod = []
    for map in maps:
        bod.append(list(map))
    H, W = len(bod), len(bod[0])
    
    sy, sx = 0, 0
    ly, lx = 0, 0
    for row, col in product(range(H), range(W)):
        if bod[row][col] == 'S':
            sy, sx = row, col
        if bod[row][col] == 'L':
            ly, lx = row, col

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
            
    q = deque([(sy, sx, 0)])
    visited = [[False]*W for _ in range(H)]
    answer1 = -1
    while q:
        y, x, cnt = q.popleft()
        
        if bod[y][x]=='L':
            answer1 = cnt
            break
        
        for u, v in zip(dy, dx):
            ny, nx = y+u, x+v
            if 0<=ny<H and 0<=nx<W and bod[ny][nx]!='X' and visited[ny][nx]==False:
                q.append((ny, nx, cnt+1))
                visited[ny][nx] = True

    q = deque([(ly, lx, 0)])
    visited = [[False]*W for _ in range(H)]
    answer2 = -1
    while q:
        y, x, cnt = q.popleft()
        
        if bod[y][x]=='E':
            answer2 = cnt
            break
        
        for u, v in zip(dy, dx):
            ny, nx = y+u, x+v
            if 0<=ny<H and 0<=nx<W and bod[ny][nx]!='X' and visited[ny][nx]==False:
                q.append((ny, nx, cnt+1))
                visited[ny][nx] = True
    
    if answer1 == -1 or answer2 == -1:
        return -1
    else:
        return answer1 + answer2