from collections import deque
from itertools import product

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solution(maps):
    bod = [list(map) for map in maps]
    
    H = len(bod)
    W = len(bod[0])
    visited = [[False]*W for _ in range(H)]
    
    answer = []
    for y, x in product(range(H), range(W)):
        if bod[y][x]=='X' or visited[y][x]==True:
            continue
        q = deque([(y, x)])
        visited[y][x] = True
        cnt = int(bod[y][x])
        while q:
            y, x = q.popleft()
            for u, v in zip(dy, dx):
                ny, nx = y+u, x+v
                if 0<=ny<H and 0<=nx<W and bod[ny][nx]!='X' and not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    cnt += int(bod[ny][nx])
        answer.append(cnt)
    
    if answer:
        answer.sort()
    else:
        answer = [-1]
    
    return answer