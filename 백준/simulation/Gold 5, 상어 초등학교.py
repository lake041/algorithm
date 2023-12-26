# https://www.acmicpc.net/problem/21608

from itertools import product
from sys import stdin
input = stdin.readline

N = int(input())
bod = [[0]*N for _ in range(N)]
student = {}
for _ in range(N**2):
    a, b, c, d, e = map(int, input().split())
    student[a] = (b, c, d, e)

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for s in student:
    seats = []
    for y, x in product(range(N), repeat=2):
        friend_count = 0
        blank_count = 0
        if bod[y][x] != 0:
            continue
        for u, v in zip(dy, dx):
            ny, nx = y+u, x+v
            if not(0<=ny<N and 0<=nx<N):
                continue
            if bod[ny][nx] in student[s]:
                friend_count +=1
            if bod[ny][nx] == 0:
                blank_count += 1
        seats.append((friend_count, blank_count, y, x))
    seats.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))
    y, x = seats[0][2], seats[0][3]
    bod[y][x] = s

answer = 0
for y, x in product(range(N), repeat=2):
    s = bod[y][x]
    friend_count = 0
    for u, v in zip(dy, dx):
        ny, nx = y+u, x+v
        if not(0<=ny<N and 0<=nx<N):
            continue
        if bod[ny][nx] in student[s]:
            friend_count +=1
    answer += (10**friend_count)//10
print(answer)