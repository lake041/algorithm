# https://www.acmicpc.net/problem/23290
# visited에서 물고기가 있는 칸만 냄새를 남겼어야 했다.

from copy import deepcopy
from collections import deque
from itertools import product
from sys import stdin
input = stdin.readline


# 1. input
M, S = map(int, input().split())
fish = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
sy, sx = map(lambda x: int(x)-1, input().split())
bod = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0]*4 for _ in range(4)]

for f in fish:
    y, x, d = f
    bod[y][x].append(d)

# 2. define functions
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

def fish_move():
    global sy, sx, bod
    temp = [[[] for _ in range(4)] for _ in range(4)]
    fish_list = []
    for y, x in product(range(4), repeat=2):
        for direction in bod[y][x]:
            fish_list.append((y, x, direction))
    
    for f in fish_list:
        fy, fx, direction = f
        for i in range(8):
            new_direction = (direction-i)%8
            ny = fy + dy[new_direction]
            nx = fx + dx[new_direction]
            if 0<=ny<4 and 0<=nx<4 and (ny, nx)!=(sy, sx) and smell[ny][nx]==0:
                temp[ny][nx].append(new_direction)
                break
            if i==7:
                temp[fy][fx].append(direction)
    bod = temp

my = [-1, 0, 1, 0]
mx = [0, -1, 0, 1]

def shark_move():
    global sy, sx
    route_list = []
    q = deque()
    q.append((sy, sx, 0, 0, []))
    while q:
        y, x, depth, count, visited = q.popleft()
        if depth == 3:
            route_list.append((y, x, depth, count, visited))
            continue

        depth += 1
        for i in range(4):
            ny, nx = y+my[i], x+mx[i]
            if not(0<=ny<4 and 0<=nx<4):
                continue
            if (ny, nx) in visited:
                q.append((ny, nx, depth, count, visited+[(ny, nx)]))
            else:
                q.append((ny, nx, depth, count+len(bod[ny][nx]), visited+[(ny, nx)]))

    route_list.sort(key = lambda x : -x[3])
    route = route_list[0]
    visited = route[4]
    for y, x in visited:
        if len(bod[y][x]) >= 1:
            smell[y][x] = 3
            bod[y][x] = []
    sy, sx = visited[2]

def remove_smell():
    for y, x in product(range(4), repeat=2):
        if smell[y][x] >= 1:
            smell[y][x] -= 1

def copy(initial):
    for y, x in product(range(4), repeat=2):
        for direction in initial[y][x]:
            bod[y][x].append(direction)

def answer():
    answer = 0
    for y, x in product(range(4), repeat=2):
        answer += len(bod[y][x])
    print(answer)

# 3. get answer
for i in range(S):
    initial = deepcopy(bod)    
    fish_move()
    shark_move()
    remove_smell()
    copy(initial)
answer()
'''
7 1
4 3 5
1 3 5
2 4 2
2 1 6
3 4 4
3 4 4
3 4 4
4 2
'''