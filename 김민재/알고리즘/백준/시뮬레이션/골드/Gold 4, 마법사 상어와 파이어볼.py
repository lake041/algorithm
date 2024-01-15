# https://www.acmicpc.net/problem/20056
# 문제를 똑바로 읽자

from itertools import product
from collections import deque
from sys import stdin
input = stdin.readline

N, M, K = map(int, input().split())
fire_list = [list(map(int, input().split())) for _ in range(M)]
bod = [[deque() for _ in range(N)] for _ in range(N)]

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

# 파이어볼이 겹칠 떄
def fire_hap(fire_list):
    r = fire_list[0][0]
    c = fire_list[0][1]
    temp = deque()
    temp.extend(bod[r][c])
    bod[r][c] = deque()
    m = int(sum([fire[2] for fire in temp])/5)
    s = int(sum([fire[3] for fire in temp])/len(temp))
    even = True
    directions = [fire[4]%2 for fire in temp]
    for direction in directions:
        if direction != directions[0]:
            even = False

    if m == 0:
        return
    elif even:
        for i in range(4):
            bod[r][c].append([r, c, m, s, i*2])
    else:
        for i in range(4):
            bod[r][c].append([r, c, m, s, i*2+1])

# 파이어볼이 움직임
def fire_move(fire):
    r, c, m, s, d = fire
    r = (r + dy[d]*s)%N
    c = (c + dx[d]*s)%N
    bod[r][c].append([r, c, m, s, d])

for fire in fire_list:
    r, c, m, s, d = fire
    bod[r-1][c-1].append([r-1, c-1, m, s, d])

for _ in range(K):
    d = deque()
    for row, col in product(range(N), repeat=2):
        d.extend(bod[row][col])
        bod[row][col] = deque()
    while d:
        fire = d.popleft()
        fire_move(fire)
    for row, col in product(range(N), repeat=2):
        if len(bod[row][col]) >= 2:
            fire_hap(bod[row][col])

d = deque()
for row, col in product(range(N), repeat=2):
    d.extend(bod[row][col])
    bod[row][col] = deque()

ans = 0
while d:
    ans += d.popleft()[2]
print(ans)

'''
4 9 5
3 2 8 5 2
3 3 19 3 4
3 1 7 1 1
4 4 6 4 0
2 1 6 2 5
4 3 9 4 3
2 2 16 1 2
4 2 17 5 3
3 4 3 5 7
33
'''