from sys import maxsize
from collections import deque
from itertools import product

def solution(bod):
    R, C = len(bod), len(bod[0])
    rsy, rsx, bsy, bsx, rty, rtx, bty, btx = 0, 0, 0, 0, 0, 0, 0, 0
    wall = []
    
    for y, x in product(range(R), range(C)):
        if bod[y][x] == 1: rsy, rsx = y, x
        if bod[y][x] == 2: bsy, bsx = y, x
        if bod[y][x] == 3: rty, rtx = y, x
        if bod[y][x] == 4: bty, btx = y, x
        if bod[y][x] == 5: wall.append((y, x))

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    def bfs(y, x, visited, cy, cx, ty, tx):
        nonlocal R, C
        return_list = []
        for u, v in zip(dy, dx):
            ny, nx = y+u, x+v
            if  0<=ny<R and 0<=nx<C and \
                (ny, nx) not in wall and \
                (ny, nx) not in visited and \
                (ny, nx) != (cy, cx):
                is_end = (ny, nx)==(ty, tx)
                return_list.append((ny, nx, visited+[(ny, nx)], is_end))
        return return_list
    
    k = 0
    ans = maxsize
    q = deque([(rsy, rsx, [(rsy, rsx)], False, bsy, bsx, [(bsy, bsx)], False, 0)])
    while q:
        ry, rx, rv, rend, by, bx, bv, bend, cnt = q.popleft()
        if rend and bend:
            ans = min(ans, cnt)
            continue
        
        if rend:
            result = bfs(by, bx, bv, ry, rx, bty, btx)
            for y, x, v, end in result:
                q.append((ry, rx, rv, rend, y, x, v, end, cnt+1))
            continue
            
        if bend:
            result = bfs(ry, rx, rv, by, bx, rty, rtx)
            for y, x, v, end in result:
                q.append((y, x, v, end, by, bx, bv, bend, cnt+1))
            continue
        
        result11 = bfs(ry, rx, rv, by, bx, rty, rtx) # red 움직임
        for rry, rrx, rrv, rrend in result11:
            result12 = bfs(by, bx, bv, rry, rrx, bty, btx) # red 움직임 이후 blue 움직임
            for bby, bbx, bbv, bbend in result12:
                if (rry, rrx, rrv, rrend, bby, bbx, bbv, bbend, cnt+1) not in q:
                    q.append((rry, rrx, rrv, rrend, bby, bbx, bbv, bbend, cnt+1))
            
        result21 = bfs(by, bx, bv, ry, rx, bty, btx) # blue 움직임
        for bby, bbx, bbv, bbend in result21:
            result22 = bfs(ry, rx, rv, bby, bbx, rty, rtx) # blue 움직임 이후 red 움직임
            for rry, rrx, rrv, rrend in result22:
                if (rry, rrx, rrv, rrend, bby, bbx, bbv, bbend, cnt+1) not in q:
                    q.append((rry, rrx, rrv, rrend, bby, bbx, bbv, bbend, cnt+1))

    return ans if ans != maxsize else 0