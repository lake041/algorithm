from collections import deque
from itertools import product

T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    bod = [list(input()) for _ in range(H)]
    keys = list(input())
    start_set = set()
    doors = []
    ans = 0

    # start_set, doors 구성
    for row, col in product(range(H), range(W)):
        if row in [0, H-1] or col in [0, W-1]:
            char = bod[row][col]
            dot = (row, col)
            if char == '*':
                pass
            elif char.isupper() and char.lower() in keys:
                start_set.add(dot)
                bod[row][col] = '.'
            elif char.isupper() and char.lower() not in keys:
                doors.append(dot)
            elif char.islower():
                start_set.add(dot)
                keys.append(char)
                bod[row][col] = '.'
            elif char == '$':
                start_set.add(dot)
                bod[row][col] = '.'
                ans += 1
            elif char == '.':
                start_set.add(dot)

    # 먼저 start 위치에서 시작하면서 쭉 bfs로 방문한다.
    # 못 여는 문의 위치를 체크한다.
    # bfs 종료 이후 못 여는 문들을 체크하면서 열 수 있다면 다시 bfs 시행한다.
    # 계속 반복한다.
    # 만약 못 여는 문이 더이상 존재하지 않거나 못 여는 문의 변화가 없을 때 종료한다.

    visited = [[False]*W for _ in range(H)]
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    # 시작
    for start in start_set:
        y, x = start
        q = deque([(y, x)])
        visited[y][x] = True
        while q:
            y, x = q.popleft()
            for u, v in zip(dy, dx):
                ny, nx = y+u, x+v
                if 0<=ny<H and 0<=nx<W and not visited[ny][nx] and bod[ny][nx]!='*':
                    char = bod[ny][nx]
                    if char.isupper() and char.lower() not in keys:
                        doors.append((ny, nx))
                        continue
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    if char == '$':
                        ans += 1
                    if char.islower():
                        keys.append(char)
    
    while True:
        changed = False
        new_doors = []
        for start in doors:
            y, x = start
            char = bod[y][x]
            if char.lower() not in keys:
                new_doors.append((y, x))
                continue

            changed = True

            q = deque([(y, x)])
            visited[y][x] = True
            while q:
                y, x = q.popleft()
                for u, v in zip(dy, dx):
                    ny, nx = y+u, x+v
                    if 0<=ny<H and 0<=nx<W and not visited[ny][nx] and bod[ny][nx]!='*':
                        char = bod[ny][nx]
                        if char.isupper() and char.lower() not in keys:
                            new_doors.append((ny, nx))
                            continue
                        q.append((ny, nx))
                        visited[ny][nx] = True
                        if char == '$':
                            ans += 1
                        if char.islower():
                            keys.append(char)
        
        doors = new_doors

        if not changed:
            break

    print(ans)
    # print(f'                                                                 정답 {ans}')

'''
3
5 17
*****************
.............**$*
*B*A*P*C**X*Y*.X.
*y*x*a*p**$*$**$*
*****************
cz
5 11
*.*********
*...*...*x*
*X*.*.*.*.*
*$*...*...*
***********
0
7 7
*ABCDE*
X.....F
W.$$$.G
V.$$$.H
U.$$$.J
T.....K
*SQPML*
irony

1
5 9
*********
.......a*
***.*****
*$Ab*****
*********
0
'''