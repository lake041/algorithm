from collections import deque
from itertools import product

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def solution(rectangle, characterX, characterY, itemX, itemY):
    rectangle = [[lx*2, ly*2, rx*2, ry*2] for lx, ly, rx, ry in rectangle]
    characterX, characterY, itemX, itemY = characterX*2, characterY*2, itemX*2, itemY*2

    dots = set()
    for lx, ly, rx, ry in rectangle:
        for x, y in product(range(lx, rx+1), range(ly, ry+1)):
            dots.add((x, y))
    for lx, ly, rx, ry in rectangle:
        for x, y in product(range(lx+1, rx), range(ly+1, ry)):
            dots.remove((x, y)) if (x, y) in dots else None
    
    q = deque([(characterX, characterY, 0)])
    visited = set((characterX, characterY))
    
    while q:
        x, y, cnt = q.popleft()
        if (x, y) == (itemX, itemY):
            return cnt // 2
        
        for u, v in zip(dx, dy):
            nx, ny = x+u, y+v
            if (nx, ny) in dots and (nx, ny) not in visited:
                q.append((nx, ny, cnt+1))
                visited.add((nx, ny))