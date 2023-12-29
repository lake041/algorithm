from sys import maxsize
from collections import deque
from itertools import product

# 풀이 1: 풀긴 풀었는데 좀...
def solution(rectangle, characterX, characterY, itemX, itemY):
    dots = set()
    movs = set()
    for x1, y1, x2, y2 in rectangle:
        dots.add((x2, y2))
        for x in range(x1, x2):
            dots.add((x, y1))
            dots.add((x, y2))
            movs.add((x, y1, x+1, y1))
            movs.add((x+1, y1, x, y1))
            movs.add((x, y2, x+1, y2))
            movs.add((x+1, y2, x, y2))
        for y in range(y1, y2):
            dots.add((x1, y))
            dots.add((x2, y))
            movs.add((x1, y, x1, y+1))
            movs.add((x1, y+1, x1, y))
            movs.add((x2, y, x2, y+1))
            movs.add((x2, y+1, x2, y))
            
    for x1, y1, x2, y2 in rectangle:
        if x2-x1==1:
            for y in range(y1+1, y2):
                movs.discard((x1, y, x2, y))
                movs.discard((x2, y, x1, y))
        if y2-y1==1:
            for x in range(x1+1, x2):
                movs.discard((x, y1, x, y2))
                movs.discard((x, y2, x, y1))

    for x1, y1, x2, y2 in rectangle:
        for x, y in product(range(x1+1, x2), range(y1+1, y2)):
            dots.discard((x, y))
        
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
        
    answer = maxsize
    sx, sy = characterX, characterY
    tx, ty = itemX, itemY
    q = deque([(sx, sy, 0, [(sx, sy)])])
    while q:
        x, y, cnt, visited = q.popleft()
        if (x, y) == (tx, ty):
            answer = min(answer, cnt)
            if answer == 8:
                return visited
            break
        
        for u, v in zip(dx, dy):
            nx, ny = x+u, y+v
            if (nx, ny) in dots and (nx, ny) not in visited and (x, y, nx, ny) in movs:
                q.append((nx, ny, cnt+1, visited+[(nx, ny)]))
    
    return answer


# 풀이 2: 좌표를 두배한다.
'''
45678
32
_1

123456으로 진행해야 하는데 125로 진행하는 이슈가 있었다.
풀이 1에서는 너비 1짜리 rectangle에 대해 따로 movs를 제거해주는 굉장히 번거로운 작업을 했다.
풀이 2에서는 rectangle의 모든 좌표를 2배로 변환하여 1씩 이동할 때 정상 루트를 벗어나지 않도록 변경했다.
'''
def solution(rectangle, characterX, characterY, itemX, itemY):
    dots = set()
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = 2*x1, 2*y1, 2*x2, 2*y2
        for x, y in product(range(x1, x2+1), range(y1, y2+1)):
            dots.add((x, y))
            
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = 2*x1, 2*y1, 2*x2, 2*y2
        for x, y in product(range(x1+1, x2), range(y1+1, y2)):
            dots.discard((x, y))
    
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
        
    answer = maxsize
    sx, sy = 2*characterX, 2*characterY
    tx, ty = 2*itemX, 2*itemY
    q = deque([(sx, sy, 0, [(sx, sy)])])
    while q:
        x, y, cnt, visited = q.popleft()
        if (x, y) == (tx, ty):
            answer = min(answer, cnt)
            break
        
        for u, v in zip(dx, dy):
            nx, ny = x+u, y+v
            if (nx, ny) in dots and (nx, ny) not in visited:
                q.append((nx, ny, cnt+1, visited+[(nx, ny)]))
    
    return answer//2