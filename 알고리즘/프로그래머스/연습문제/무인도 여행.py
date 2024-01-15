from collections import deque
from itertools import product

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solution(bod):
    bod = [list(map(lambda x: int(x) if x.isnumeric() else 0, list(row))) for row in bod]
    R, C = len(bod), len(bod[0])
    visited = [[False]*C for _ in range(R)]

    results = []
    for y, x in product(range(R), range(C)):
        if visited[y][x] or not bod[y][x]:
            continue
        q = deque([(y, x)])
        visited[y][x] = True
        result = bod[y][x]
        
        while q:
            y, x = q.popleft()
            for u, v in zip(dy, dx):
                ny, nx = y+u, x+v
                if 0<=ny<R and 0<=nx<C and not visited[ny][nx] and bod[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    result += bod[ny][nx]
                    
        results.append(result)
    
    return sorted(results) if results else [-1]