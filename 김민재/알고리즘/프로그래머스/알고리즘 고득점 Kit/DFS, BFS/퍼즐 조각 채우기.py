from collections import deque
from itertools import product

# 90도 회전: (x, y) => (-y, x)
# BFS보다는 구현이 더 핵심인 것 같다.

def solution(game_board, table):
    L = len(game_board)

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    collections = []
    visited = [[False]*L for _ in range(L)]
    for y, x in product(range(L), range(L)):
        if table[y][x]==0 or visited[y][x]:
            continue

        dots = [(0, 0)]
        q = deque([(y, x)])
        visited[y][x] = True

        while q:
            qy, qx = q.popleft()
            for u, v in zip(dy, dx):
                ny, nx = qy+u, qx+v
                if 0<=ny<L and 0<=nx<L and table[ny][nx]==1 and not visited[ny][nx]:
                    dots.append((ny-y, nx-x))
                    q.append((ny, nx))
                    visited[ny][nx] = True
        
        # (x, y) => (-y, x)
        rotate0 = sorted(dots)
        rotate90 = sorted([(tx, -ty) for ty, tx in rotate0])
        rotate180 = sorted([(tx, -ty) for ty, tx in rotate90])
        rotate270 =  sorted([(tx, -ty) for ty, tx in rotate180])
        collection = [rotate0, rotate90, rotate180, rotate270]
        collections.append(collection)
    
    used = [False]*len(collections)
    answer = 0

    for y, x in product(range(L), range(L)):
        if game_board[y][x] == 1:
            continue

        visited = [[False]*L for _ in range(L)]

        dots = [(0, 0)]
        q = deque([(y, x)])
        visited[y][x] = True

        while q:
            qy, qx = q.popleft()
            for u, v in zip(dy, dx):
                ny, nx = qy+u, qx+v
                if 0<=ny<L and 0<=nx<L and game_board[ny][nx]==0 and not visited[ny][nx]:
                    dots.append((ny-y, nx-x))
                    q.append((ny, nx))
                    visited[ny][nx] = True
        
        dots.sort()

        for i in range(len(collections)):
            if used[i]:
                continue
            collection = collections[i]
            same = False
            for piece in collection:
                if dots == piece:
                    same = True
                    used[i] = True
                    for zy, zx in dots:
                        game_board[y+zy][x+zx] = 1
                    answer += len(piece)
                    break
            if same:
                break

    return answer