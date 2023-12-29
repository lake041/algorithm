from collections import deque
from itertools import product

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solution(land):
    R, C = len(land), len(land[0])
    visited = [[False]*C for _ in range(R)]
    memo = [0]*C
    
    for cy, cx in product(range(R), range(C)):
        if visited[cy][cx] or land[cy][cx]==0:
            continue
        
        cols = set()
        cnt = 0
        
        q = deque([(cy, cx)])
        visited[cy][cx] = True
        cnt += 1
        cols.add(cx)
        while q:
            y, x = q.popleft()
            for u, v in zip(dy, dx):
                ny, nx = y+u, x+v
                if 0<=ny<R and 0<=nx<C and not visited[ny][nx] and land[ny][nx]==1:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    cnt += 1
                    cols.add(nx)

        for x in cols:
            memo[x] += cnt

    return max(memo)