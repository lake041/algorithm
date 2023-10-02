from itertools import product
from sys import stdin
input = stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def fishing(col):
    global bod, answer
    for i in range(R):
        if bod[i][col][2] > 0:
            answer += bod[i][col][2]
            bod[i][col] = (0, 0, 0)
            break

def shark_all_move():
    global bod
    temp = [[[] for _ in range(C)] for _ in range(R)]
    for y, x in product(range(R), range(C)):
        if bod[y][x] == (0, 0, 0):
            continue
        s, d, z = bod[y][x]
        shark_move(temp, y, x, s, d, z)
    shark_eat(temp)
    bod = temp

def shark_move(temp, y, x, s, d, z):
    ny, nx = y, x
    for _ in range(s):
        ny, nx = ny+dy[d], nx+dx[d]
        if not (0<=ny<R and 0<=nx<C):
            d = (d+2)%4
            ny, nx = ny+dy[d]+dy[d], nx+dx[d]+dx[d]
    temp[ny][nx].append((s, d, z))

def shark_eat(temp):
    for y, x in product(range(R), range(C)):
        if not temp[y][x]:
            temp[y][x] = (0, 0, 0)
            continue
        temp[y][x].sort(key = lambda x : -x[2])
        temp[y][x] = temp[y][x][0]

R, C, M = map(int, input().split())
bod = [[(0, 0, 0) for _ in range(C)] for _ in range(R)]
shark = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    # 1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽
    # 1: 0, 3: 1, 2: 2, 4: 3
    if d==1: d = 0
    elif d==2: d = 2
    elif d==3: d = 1
    elif d==4: d = 3
    bod[r-1][c-1] = (s, d, z)

answer = 0
for i in range(C):
    fishing(i)
    shark_all_move()
print(answer)