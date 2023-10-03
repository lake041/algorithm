# https://www.acmicpc.net/problem/2638
# 외부 공기는 BFS 수행시 격자 밖으로 나가면서 종료되고
# 내부 공기는 치즈를 만나면서 종료된다.

from collections import deque
from itertools import product
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# outer air: 0
# cheese: 1
# inner air: 2
def find_inner():
    visited = [[False]*M for _ in range(N)]
    inner, outer = [], []
    for y, x in product(range(N), range(M)):
        if bod[y][x] == 1:
            visited[y][x] = True
        if visited[y][x] == True:
            continue

        temp = []
        type = 'inner'

        # (y, x)도 넣어야지
        q = deque()
        q.append((y, x))
        visited[y][x] = True
        temp.append((y, x))
        while q:
            ty, tx = q.popleft()
            for u, v in zip(dy, dx):
                ny, nx = ty+u, tx+v
                # 격자 밖으로 나가면 외부 공기
                # nx 범위
                if not(0<=ny<N and 0<=nx<M):
                    type = 'outer'
                    continue
                if visited[ny][nx]==False and bod[ny][nx]!=1:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    temp.append((ny, nx))
        if type == 'inner':
            inner = inner + temp
        if type == 'outer':
            outer = outer + temp
    
    for y, x in inner:
        bod[y][x] = 2
    for y, x in outer:
        bod[y][x] = 0

def melt():
    melt_list = []
    for y, x in product(range(N), range(M)):
        count = 0
        if bod[y][x] != 1:
            continue
        for u, v in zip(dy, dx):
            ny, nx = y+u, x+v
            if 0<=ny<N and 0<=nx<M and bod[ny][nx]==0:
                count += 1
        if count >= 2:
            melt_list.append((y, x))
    for y, x in melt_list:
        bod[y][x] = 0

def end():
    for y, x in product(range(N), range(M)):
        if bod[y][x] == 1:
            return False
    return True

time = 0
while True:
    if end():
        break
    time += 1
    find_inner()
    melt()

print(time)

'''
8 9
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 0 1 1 0 1 1 0
0 0 1 1 1 1 1 1 0
0 0 1 1 1 1 1 0 0
0 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
4

8 9
2 2 2 2 2 2 2 2 2
2 2 2 1 1 2 2 2 2
2 2 2 1 1 2 1 1 2
2 2 1 1 1 1 1 1 2
2 2 1 1 1 1 1 2 2
2 2 1 1 2 1 1 2 2
2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2
4

8 9
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 1 1 0
0 1 0 1 1 1 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 1 1 1 0 1 0
0 1 1 0 0 0 1 1 0
0 0 0 0 0 0 0 0 0
3
'''