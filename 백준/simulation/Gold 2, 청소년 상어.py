# https://www.acmicpc.net/problem/19236
# BOARD_SIZE = 4니까 그냥 하나씩 다 탐색해봐도 될 것 같다.

from copy import deepcopy
from collections import deque
from itertools import product
from sys import stdin
input = stdin.readline

BOARD_SIZE = 4

# 12시 방향부터 반시계 방향으로 회전
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

# one fish 움직임
def one_fish_move(bod, y, x):
    size, direction, type = bod[y][x]
    for i in range(8):
        new_direction = (direction + i) % 8
        ny = y + dy[new_direction]
        nx = x + dx[new_direction]
        if 0<=ny<BOARD_SIZE and 0<=nx<BOARD_SIZE and bod[ny][nx][2]!=1:
            bod[y][x][1] = new_direction
            bod[y][x], bod[ny][nx] = bod[ny][nx], bod[y][x]
            return

# all fish 움직임
def all_fish_move(bod):
    for i in range(1, 17):
        for y, x in product(range(BOARD_SIZE), repeat=2):
            if bod[y][x][2] == 1:
                continue
            if bod[y][x][0] == i:
                one_fish_move(bod, y, x)
                break

# get target
def get_target(direction, sy, sx, bod):
    target = []
    for i in range(1, BOARD_SIZE):
        ny = sy + dy[direction]*i
        nx = sx + dx[direction]*i
        if 0<=ny<BOARD_SIZE and 0<=nx<BOARD_SIZE and bod[ny][nx][2]==0:
            target.append([ny, nx])
    return target

# 냠냠
def eat(sy, sx, ty, tx, bod):
    global answer
    target_size, target_direction, target_type = bod[ty][tx]
    shark_size, shark_direction, shark_type = bod[sy][sx]
    bod[ty][tx] = [shark_size + target_size, target_direction, 1]
    bod[sy][sx] = [0, 0, 2]
    answer = max(answer, shark_size + target_size)


# bod 입력
bod = []
for _ in range(BOARD_SIZE):
    temp = list(map(int, input().split()))
    row = []
    for i in range(0, 8, 2):
        row.append([temp[i], temp[i+1]-1, 0])
    bod.append(row)

# initiate
first_target = bod[0][0]
bod[0][0] = [first_target[0], first_target[1], 1]
all_fish_move(bod)

# start bfs
global answer
answer = max(0, first_target[0])
q = deque()
q.append([0, 0, bod])
while q:
    sy, sx, bod = q.popleft()
    targets = get_target(bod[sy][sx][1], sy, sx, bod)
    if targets:
        for ty, tx in targets:
            new_bod = deepcopy(bod)
            eat(sy, sx, ty, tx, new_bod)
            all_fish_move(new_bod)
            q.append([ty, tx, new_bod])
print(answer)