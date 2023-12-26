# https://www.acmicpc.net/problem/21609

from collections import deque
from itertools import product
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

# -1: black, 0: rainbow, M: general
def find_block():
    # [total_count, rainbow_count, y, x]
    block_list = []
    visited = [[False]*N for _ in range(N)]
    for y, x in product(range(N), repeat=2):
        color = bod[y][x]
        if color in [-1, 0, -100] or visited[y][x]==True:
            continue
        total_count = 1
        rainbows = []
        q = deque()
        q.append((y, x))
        visited[y][x] = True
        while q:
            ty, tx = q.popleft()
            for u, v in zip(dy, dx):
                ny, nx = ty+u, tx+v
                if 0<=ny<N and 0<=nx<N and visited[ny][nx]==False and bod[ny][nx] in [0, color] :
                    total_count += 1
                    if bod[ny][nx] == 0:
                        rainbows.append((ny, nx))
                    q.append((ny, nx))
                    visited[ny][nx] = True
        if total_count >= 2:
            block_list.append([total_count, len(rainbows), y, x])
        for ry, rx in rainbows:
            visited[ry][rx] = False
    block_list.sort(key = lambda x : (-x[0], -x[1], -x[2], -x[3]))

    return block_list[0] if len(block_list) > 0 else 'End'

def remove_block(ref):
    global answer
    total_count, rainbow_count, y, x = ref
    answer += total_count**2
    color = bod[y][x]
    q = deque()
    q.append((y, x))
    bod[y][x] = -100
    while q:
        y, x = q.popleft()
        for u, v in zip(dy, dx):
            ny, nx = y+u, x+v
            if 0<=ny<N and 0<=nx<N and bod[ny][nx] in [0, color]:
                q.append((ny, nx))
                bod[ny][nx] = -100

def drop():
    for _ in range(20):
        for y in range(N-2, -1, -1):
            for x in range(N):
                if bod[y][x] == -1:
                    continue
                if bod[y+1][x] == -100:
                    bod[y][x], bod[y+1][x] = bod[y+1][x], bod[y][x]

def rotate():
    global bod
    bod = list(map(list, zip(*bod)))[::-1]

answer = 0
while True:
    result = find_block()
    if result == 'End':
        break
    remove_block(result)
    drop()
    rotate()
    drop()
print(answer)